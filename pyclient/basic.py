"""Consuming the API"""
import requests

END_POINT="http://127.0.0.1:8000/"
response=requests.post(END_POINT, json={"category":1,"name":"one"})

print(response.json())

