#!/usr/bin/env python3
import os,json
'''
#Q1
print("Content-Type: text/plain")
print()
print(os.environ)


#Q2
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent = 4))

print("Content-Type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
'''
#Q3
print("Content-Type: text/html")
print()
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")
