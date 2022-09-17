"""Fetching the products details"""
import requests

END_POINT="http://127.0.0.1:8000/api/products/3/"
response=requests.get(END_POINT)

print(response.json())

