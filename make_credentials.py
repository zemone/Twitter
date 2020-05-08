import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 'XXXXXX'
credentials['CONSUMER_SECRET'] = 'XXXXXX'
credentials['ACCESS_TOKEN'] = 'XXXXXX'
credentials['ACCESS_SECRET'] = 'XXXXXX'

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)