import csv
import random
import authenticate as auth
import hashlib
import Passwords

email = input("What is your email")
password = input("What is your password")

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
    email = hashlib.sha512(email.encode()).hexdigest()
    password = hashlib.sha256(password.encode()).hexdigest()
    with open('user.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow((email, password))
else:
    print("code is wrong")



