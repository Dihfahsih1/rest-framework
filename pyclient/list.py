"""Fetching all the created products"""
import requests

END_POINT="http://127.0.0.1:8000/api/products/"
response=requests.get(END_POINT)

print(response.json())
