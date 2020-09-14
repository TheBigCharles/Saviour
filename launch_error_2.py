import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 

fromaddr = 'felix_test_mail@yeah.net'

password = 'test223'

toaddrs = ['felix_test_mail@yeah.net']

content = 'Sorry, there is an error with the file. [PermissionError]'

textApart = MIMEText(content)

m = MIMEMultipart()

m.attach(textApart)

m['Subject'] = '[PermissionError]'


try:

        server = smtplib.SMTP('smtp.yeah.net')

        server.login(fromaddr,password)

        server.sendmail(fromaddr, toaddrs, m.as_string())

        server.quit()

except smtplib.SMTPException as e:

        pass


