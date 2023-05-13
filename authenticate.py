import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import Passwords


def send_email(sender_email, receiver_email, code6password):
    # email content
    subject = "Authentication"
    body = str(code6password)



    # create a message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # add body to the message
    message.attach(MIMEText(body, "plain"))

    # create a SMTP session
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        # identify ourselves to the server
        server.ehlo()
        # encrypt the connection
        server.starttls()
        # identify ourselves again
        server.ehlo()
        # login to the email account
        server.login(sender_email, Passwords.password)
        # send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
