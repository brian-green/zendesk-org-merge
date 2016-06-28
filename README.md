# Zendesk Organization Merge

Zendesk can't merge organizations like tickets and users. This tool allows you to move users and their tickets from one organization to another; even closed tickets.

## How the app works

This is a command line tool created with stock Python features and the Zendesk API.

The app utilizes the multiple organizations feature to put a user in both organizations, then copies over all of their tickets from organization 1 to organization 2 using the ticket imports API.

After the data has been migrated, the old tickets, users, and the "from" organization are deleted.

## Caveats

Please note that this solution may not fit all account scenarios. Since closed tickets are deleted from one organization; old links to tickets in Help Center will no longer work for end users. Users can still navigate to their tickets in Help Center however. For accounts that are email support only then this is largely a non-issue.