# Day 7: Project Day + Bonus API Intro
# •	- Mini Project Completion
# •	- Introduction to APIs
# •	- Final Project Submission Guidelines
# •	- Q&A Session and Bootcamp Wrap-up

import requests
import os

from dotenv import load_dotenv

load_dotenv()

key = os.environ['api_key']
password = os.environ['password']

# url = "http://api.open-notify.org/iss-now.json"

# Api Endpoint
url = "https://newsapi.org/v2/everything"

# query addition
parameter = {
    "apikey": key,
    "q":"tesla"
}

# response handle
response = requests.get(url,params= parameter)

# Data extraction
data = response.json()
print(data)


