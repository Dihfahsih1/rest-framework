"""Delete the product """
import requests

PRODUCT_ID=input("Enter the id you want to delete \n: ")

try:
  PRODUCT_ID=(PRODUCT_ID)
except:
  print(f'{PRODUCT_ID} is not a valid ID')
if PRODUCT_ID:
  END_POINT=f"http://127.0.0.1:8000/api/products/{PRODUCT_ID}/delete/"
  data = {
    "title":"Potatoes",
    "price":2000,
  }
  response=requests.delete(END_POINT, json=data)

  print(response.status_code, response.status_code==204)