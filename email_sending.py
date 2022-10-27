from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'nithin.bvn.dec25@gmail.com'
email_password = password

email_receiver = 'caraca4703@3mkz.com'

subject = "This is the test of the python email sender project"

body = """
When you receive the mail in the inbox, project works!
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

conte = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=conte) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
