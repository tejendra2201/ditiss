#!/usr/bin/python3

import sys
import requests

h = sys.argv[2]+"/.json"

r = requests.get(h)
code = r.status_code

resp = requests.put(h+"/.json", data = {'key':'value'})

if code == 200:
    print("Text is readable")
else:
    print("Text is not readable")

status = resp.status_code
if status == 200:
    print("Text is writeable")
else:
    print("Text is not writeable")
