#!/usr/bin/env python3
import cgi,cgitb
cgitb.enable()
from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

#create instance of FieldStorage
form = cgi.FieldStorage()

#Get data from fields
username = form.getfirst('username')
password = form.getfirst('password')
print("Content-type:text/html\r\n\r\n")
print()

Username = None
Password = None
if username == secret.username and password == secret.password:
    C = SimpleCookie()
    C['Username'] = username
    C['Password'] = password
    Username = C['Username'].value
    Password = C['Password'].value

user_id = None
pass_word = None
if 'HTTP_COOKIE' in os.environ:
    print(f"<p>HTTP_COOKIE={os.environ['HTTP_COOKIE']}</p>")    
    cookie_string=os.environ.get('HTTP_COOKIE')
    if cookie_string:
        c = cookie_string.split('; ')
        for i in c:
            (key, value) = i.split('=')
            if key == "Username":
                user_id = value
            if key == "Password":
                pass_word = value

if user_id==secret.username and pass_word==secret.password:
    print(secret_page(username,password))
elif not username and not password:
    print(login_page())
elif username == Username and password == Password:
    print(secret_page(secret.username,secret.password))
else:
    print(after_login_incorrect())