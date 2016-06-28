# 1. Grab organization membership

## import libraries
import requests
import json

## defining variables for authentication
subdomain = raw_input("Enter subdomain > ")
organization = raw_input("Enter org ID > ")
admin = raw_input("Enter email > ")
api_token = raw_input("Enter API Token > ")

## modifies admin string to use API token
admin = admin + '/token'

## Create URL for organization membership request 
membership_url = \
'https://' + subdomain + '.zendesk.com/api/v2/organizations/' + \
organization + '/organization_memberships.json'

## Request for organization membership data
membership_request = requests.get(membership_url, \
auth = (admin, api_token)).json()

## List for holding user ids
users = []

## loop through organization membership and add user ids to users list
for item in membership_request['organization_memberships']:
	requester = item["user_id"]
	users.append(requester)

	# 2. Make list of tickets for users
	for user in users:
	
		## create URL for requested tickets by user
		tickets_url = \
		'https://' + subdomain + '.zendesk.com/api/v2/users/' + \
		str(user) + '/tickets/requested.json'

		## Request for tickets
		tickets_request = requests.get(tickets_url, \
		auth = (admin, api_token)).json()

		## List for tickets
		tickets = []

		## Loop through ticket data ticket ids to ticket list
		for ticket in tickets_request['tickets']:
			tickets.append(ticket['id'])
	
	# print(tickets)

		# 3. Grab ticket meta data and comment data.
		for ticket_id in tickets:
			
			## meta data URL
			meta_url = \
			'https://' + subdomain + '.zendesk.com/api/v2/tickets/' + \
			str(ticket_id) + '.json'

			## meta request
			meta_request = requests.get(meta_url, \
			auth = (admin, api_token)).json()

			## comment URL
			comment_url = \
			'https://' + subdomain + '.zendesk.com/api/v2/tickets/' + \
			str(ticket_id) + '/comments.json'

			## comment request
			comment_request = requests.get(comment_url, \
			auth = (admin, api_token)).json()

		# testing	
		# print(meta_request['ticket']['subject'])
		# print(comment_request['comments'][0]['body'])

			#4. Create JSON object for ticket import
			
			## repository for comments on tickets
			comment_list = []

			## Creating a string of comment data, putting into a list
			for c in comment_request['comments']:
				comment_list.append('{"author_id": ' + str(c['author_id']) + \
				', "value": ' + c['body'] + ', "created_at": ' \
				+ c['created_at'] + '}, "public": ' + str(c['public']) + '}')

			## testing spot check for formatting 
			print(comment_list[0])




























