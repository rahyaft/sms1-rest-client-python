#Please install the 'requests' module (for example, using "pip install requests")
import requests

# SMS1 API base URL
api_base_url = 'https://SubDomain.Domain:Port/api/service/'

# The API name according to SMS1.ir
# api_name = 'patternSend'
api_name = 'patternSend'

# Token is received from SMS1.ir
token = 'YOUR_TOKEN'

# Setting the HTTP request headers
request_headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

# Sample input model for API 'send'
# request_body = {'Message': 'سلام', 'Recipient': '09120000000'}

# Sample input model for API 'patternSend'
# PatternId: received from SMS1.ir
# Pairs: holds the variables that exist in the approved pattern of your Token
request_body = {'PatternId': 7, 'Recipient': '09120000000', 'Pairs': {'variable_1': 'value_1', 'variable_2': 'value_2'}}

# Sending the request
response = requests.post(api_base_url + api_name, json = request_body, headers = request_headers)

print(response.status_code)
