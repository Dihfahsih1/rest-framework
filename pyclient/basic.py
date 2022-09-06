import requests

endpoint="http://127.0.0.1:8000/api"
response=requests.get(endpoint, json={"Product_id":123})
 
print(response.json()) #body of the response returned 
'''Normal http requests return html but REST API HTPP Request returns JSON or xml'''

 

 