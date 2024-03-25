# Sending a post request with python to the api
# Any language can be used to do this, the api is gonna reply.

import requests
url = "http://127.0.0.1:8821/webhookpost"

while True:
    content = input("enter message: ")
    x = requests.post(url, json={"message":f"{content}"})
    print(x.status_code)