# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
  
# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import os
import csv
import getpass
from titlecase import titlecase

# creates SMTP session 
session = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security 
session.starttls()   
# Authentication 
fromaddr = input('Enter sender email address : ')
session.login(fromaddr, getpass.getpass(prompt = 'Enter sender password : ')) 
#toaddr = "shuvankarroy2@gmail.com"
# instance of MIMEMultipart 


directory = 'path containing all certificates created by script (create_certificate.py)'

          
for (subdir, dirs, filenames) in os.walk(directory):
        for file in filenames:
                filename = subdir + os.sep + file
                print(filename)
                msg = MIMEMultipart()
                participantName, toaddr = filename.rsplit('\\' , -1)[4][:-4].rsplit("-")
                # storing the senders email address,  storing the receivers email address
                msg['From'], msg['To'] = fromaddr, toaddr
                # storing the subject  
                msg['Subject'] = "Quizzare\'19 Participation Certificate"
                # attach the body with the msg instance 
                msg.attach(MIMEText("Dear "+ participantName +", \nMessage (optional)", 'plain')) 
                # open the file to be sent  
                # instance of MIMEBase and named as p 
                p = MIMEBase('application', 'octet-stream')
        
                # To change the payload into encoded form 
                p.set_payload(open(filename, "rb").read()) 
        
                # encode into base64 
                encoders.encode_base64(p) 
                p.add_header('Content-Disposition', "attachment; filename= "+participantName+"-"+toaddr+".png")
                # attach the instance 'p' to instance 'msg' 
                msg.attach(p)
                # Converts the Multipart msg into a string 
                text = msg.as_string() 
        
                # sending the mail 
                sendMail_output = session.sendmail(fromaddr, toaddr, text)
           
# terminating the session 
session.quit() 
