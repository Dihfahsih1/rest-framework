"""Fetching all the created products"""
import requests
from getpass import getpass

AUTH_END_POINT = "http://127.0.0.1:8000/api/auth/"
PASSWORD = getpass()
response=requests.post(AUTH_END_POINT, json={'username':'admin', 'password':PASSWORD})

print(response.json())

