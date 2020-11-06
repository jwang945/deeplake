import requests
from requests.exceptions import HTTPError

url = "https://cat-fact.herokuapp.com/facts" #edit URL to pick which api to retrieve data from

try:
    response = requests.get(url)
    print(response.text)
    # If the response was successful, no Exception will be raised
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')