import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import socket
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

#from email.mime.multipart import MIMEMultipart
#from email.MIMEText import MIMEText

fromaddr = "piraspberry915@gmail.com"
toaddr = "rfeldman@bates.edu"
msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ip address test"

body = host_ip
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "raspberry!")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
toaddr = "rfeldman@bates.edu"
msg['To']= toaddr
server.sendmail(fromaddr, toaddr, text)
toaddr = "ptakle@bates.edu"
msg['To']= toaddr
server.sendmail(fromaddr, toaddr, text)
server.quit()
