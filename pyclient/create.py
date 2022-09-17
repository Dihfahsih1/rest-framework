"""Fetching the products details"""
import requests

END_POINT="http://127.0.0.1:8000/api/products/"
data={"title":"beans",
      "price":5000,}
response=requests.post(END_POINT, json=data)

print(response.json())

