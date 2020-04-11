import smtplib, ssl
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

port = 465
smtp_server = "smtp.gmail.com"
sender_email = " Sender Email "
receiver_email = " Receiver Email "
password = " Sender Password "
body = """ Email Body """

# instance of MIMEMultipart 
msg = MIMEMultipart()

# storing the subject  
msg['Subject'] = " Email Subject "

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain'))

# File Part Starts From Here
  
# open the file to be sent  
filename = " Attachment File Name "
attachment = open(" Attachemtn File Directory ", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p)

#File Part Ends Here. If You Don't Need to Attach File, You Can Remove This Part
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls()
  
# Converts the Multipart msg into a string 
text = msg.as_string()


temp = 0

while (temp < 1):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        temp = temp + 1
        print(temp)

print ('Successful')
