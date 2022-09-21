"""Fetching the products details"""
import requests

END_POINT="http://127.0.0.1:8000/api/products/4/details"
response=requests.get(END_POINT)

print(response.json())

