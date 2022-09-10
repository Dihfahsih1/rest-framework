import requests

endpoint="http://127.0.0.1:8000/save_sub_category"
response=requests.post(endpoint, json={"category":1,"name":"one"})
 
print(response.json()) #body of the response returned 
'''Normal http requests return html but REST API HTPP Request returns JSON or xml'''

 

 