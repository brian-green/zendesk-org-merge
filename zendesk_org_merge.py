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
membership_request = requests.get(membership_url, auth = (admin, api_token)).json()

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
		tickets_request = requests.get(tickets_url, auth = (admin, api_token)).json()

		## List for tickets
		tickets = []

		## Loop through ticket data ticket ids to ticket list
		for ticket in tickets_request['tickets']:
			tickets.append(ticket['id'])		
	
	print(tickets)

