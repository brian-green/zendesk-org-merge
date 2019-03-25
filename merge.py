# Import modules
import requests
import json

# Authentication
user = 'person@email.com/token'
token = 'TOKEN'

# Session
s = requests.Session()
s.auth = (user, token)
s.headers = {'Content-Type':'application/json'}

## Resources ##
#Global url
url = 'https://subdomain.zendesk.com/api/v2/'

# Search URL
search = 'search.json?query=type:ticket organization:360086759814'

# Ticket List
ticket_list = []
search_url = url + search

while search_url:
    response = s.get(search_url)
    data = response.json()

    for each in data['results']:
        ticket_id = each['id']
        ticket_list.append(ticket_id)
    search_url = data['next_page']

# Ticket Meta data
for each in ticket_list:
    ticket_data = s.get('https://sentinelone.zendesk.com/api/v2/tickets/' + str(each) + '.json')

    ticket_data = ticket_data.json()

    print("Modifying ticket " + str(each))
    del ticket_data['ticket']['satisfaction_probability']
    del ticket_data['ticket']['satisfaction_rating']
    ticket_data['ticket']['organization_id'] = 360837499914

    print('Getting comments for ' + str(each))
    comment_data = s.get('https://subdomain.zendesk.com/api/v2/tickets/' + str(ticket_id) + '/comments.json')
    comment_data = comment_data.json()
    comments = comment_data['comments']

    print('Making final payload')
    ticket_data['comments'] = comments
    ticket_data = json.dumps(ticket_data)

    post = s.post('https://subdomain.zendesk.com/api/v2/imports/tickets.json', data = ticket_data)

    if post.status_code == 201:
        print("Posted ticket #" + str(each))
    else:
        print("bad post")
        print(post.status_code)
        print(post.headers)
        print(post.text)
        print("-===========-")
        print(json.dumps(ticket_data))
        break
