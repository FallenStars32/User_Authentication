import random
import authenticate as auth
import hashlib
import Passwords
import connection as c
import email_encryption as ee


email = input("What is your email")
password = input("What is your password")
username = input("What username would you like to use")

code = []
fcode = ''
for i in range(6):
    i = random.randint(0, 10)
    code.append(i)

for i in code:
    fcode += str(i)


auth.send_email(Passwords.email,email, fcode)

ucode = input("What code do you want")
if ucode == fcode:
    email, key = ee.encrypt_email(email)
    password = hashlib.sha256(password.encode()).hexdigest()
    username = hashlib.sha256(username.encode()).hexdigest()

    print(key)

    c.add_user_a(username, password, email)
    c.add_user_k(key)

else:
    print("code is wrong")



