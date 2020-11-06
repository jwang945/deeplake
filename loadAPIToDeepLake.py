import requests
from requests.exceptions import HTTPError
from azure.storage.filedatalake import DataLakeServiceClient
from azure.storage.filedatalake import DataLakeFileClient
import datetime

def upload_to_DeepLake(filesystem_name, connection_string, data):
    #datalake client creation
    service = DataLakeServiceClient.from_connection_string(conn_str=connection_string)
    #filesystem_name cannot have capitol letters or /
    print("Generating file system named: ", filesystem_name)

    #create the filesystem client
    filesystem_client = service.create_file_system(file_system=filesystem_name)

    #add a file to the filesystem
    file_name = filesystem_name+"001"
    file_client = filesystem_client.get_file_client(file_name)
    file_client.create_file()
    file_client.append_data(data=data, offset=0, length=len(data))
    file_client.flush_data(len(data))
    #filesystem_client.delete_file_system() #clean the filesystem

url = "https://cat-fact.herokuapp.com/facts" #edit URL to pick which api to retrieve data from
connection_string = 'DefaultEndpointsProtocol=https;AccountName=apitodatalaketest1;AccountKey=EpEARsk4ZxdplPrq6UlfajD7ukz61A+38zWn8Lcq4sB4yXEfyBXZ8H/WhyvSaeAXpP9Dwwmp+gXFoHb53Yq3Mg==;EndpointSuffix=core.windows.net'
                    #change this to account connection string to flush data there
try:
    response = requests.get(url)
    #will only raise a response if unsuccessful
    response.raise_for_status()
    data = response.text 
    upload_to_DeepLake("herokutest7", connection_string, data) #filesystem name cannot have capital letters or /
    
    
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')

