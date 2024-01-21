import requests

# Replace 'YOUR_API_KEY' and 'API_ENDPOINT' with your actual API key and endpoint
api_key = 'AIzaSyBdEluVk5_sp43-7fz8iUOw4qdpIKzzytQ'
api_endpoint = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJrTLr-GyuEmsRBfy61i59si0&fields=address_components'

# Construct the request URL
url = f'{api_endpoint}&key={api_key}'

# Make a GET request
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    # Parse and work with the response data (JSON, XML, etc.)
    data = response.json()
    print(data)
else:
    print(f'Request failed with status code: {response.status_code}')
