#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

r = requests.get("http://httpbin.org/ip")
print r.text # Devuelve nuestra dirección IP
