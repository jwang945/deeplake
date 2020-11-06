import requests
from requests.exceptions import HTTPError
from azure.storage.filedatalake import DataLakeServiceClient

url = "https://cat-fact.herokuapp.com/facts" #edit URL to pick which api to retrieve data from
connection_string = 'DefaultEndpointsProtocol=https;AccountName=apitodatalaketest1;AccountKey=EpEARsk4ZxdplPrq6UlfajD7ukz61A+38zWn8Lcq4sB4yXEfyBXZ8H/WhyvSaeAXpP9Dwwmp+gXFoHb53Yq3Mg==;EndpointSuffix=core.windows.net'
                    #change this to account connection string to flush data there
try:
    response = requests.get(url)
    #will only raise a response if unsuccessful
    response.raise_for_status()

    #datalake client creation
    service = DataLakeServiceClient.from_connection_string(conn_str=connection_string)
    filesystem_name = "herokuTest1"
    print("Generating file system named: ", filesystem_name)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')