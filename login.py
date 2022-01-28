#!/usr/bin/env python3
import cgi,cgitb
cgitb.enable()
from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

form_ok = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

cookie_ok = cookie_username == secret.username and cookie_password == secret.password

if cookie_ok:
    username = cookie_username
    password = cookie_password

print("Content-Type: text/html")
if form_ok:
    print(f"Set-Cookie: username = {username}")
    print(f"Set-Cookie: password = {password}")
print()


if username==secret.username and password==secret.password:
    print(secret_page(username,password))
elif not username and not password:
    print(login_page())
else:
    print(after_login_incorrect())