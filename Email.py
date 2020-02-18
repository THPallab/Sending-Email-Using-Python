import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "****"   #Your Email Address
receiver_email = "***"  #Receiver Email Address
password = "***"        #Your Email Password

#Your Email With Body

message = """\          
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

print ('Successful')
