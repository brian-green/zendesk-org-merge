# Import modules
import requests
import json

# Authentication
user = 'roteml@sentinelone.com/token'
token = '9c4eepj7SBeHV4qkMWTLJNcBP0j3nSx9e6PK5bQh'

# Session
s = requests.Session()
s.auth = (user, token)
s.headers = {'Content-Type':'application/json'}

## Resources ##
#Global url
url = 'https://sentinelone.zendesk.com/api/v2/'

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
    ticket_data = s.delete('https://sentinelone.zendesk.com/api/v2/tickets/' + str(each) + '.json')
