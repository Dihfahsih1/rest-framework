"""update the product details"""
import requests

END_POINT="http://127.0.0.1:8000/api/products/1/update/"
data = {
  "title":"Potatoes",
  "price":2000,
}
response=requests.put(END_POINT, json=data)

print(response.json())

