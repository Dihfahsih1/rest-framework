"""Fetching all the created products"""
import requests
from getpass import getpass

AUTH_END_POINT = "http://127.0.0.1:8000/api/auth/"
USERNAME = input("What is your username: \n")
PASSWORD = getpass("Enter your password: \n")
auth_response=requests.post(AUTH_END_POINT, json={'username':USERNAME, 'password':PASSWORD})
print(auth_response.json())

if auth_response.status_code == 200:
  token = auth_response.json()['token']
  headers = {
    "Authorization": f"Token {token}"
             }
  END_POINT="http://127.0.0.1:8000/api/products/"
  
  get_response = requests.get(END_POINT, headers=headers)
  print(get_response.json())

