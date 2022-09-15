"""COnsuming the API"""
import requests
import basic

END_POINT="http://127.0.0.1:8000/save_sub_category"
response=requests.post(END_POINT, json={"category":1,"name":"one"})

print(response.json())

