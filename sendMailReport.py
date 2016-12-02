#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# SMTP Setting
mailHost="mail.example.com"
mailUser="user@example.com"
mailPass="password"

sender = 'user@example.com'
receivers = ['receiver@example.com']

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("SENDER_NAME", 'utf-8')
msgRoot['To'] =  Header("RECEIVER_NAME", 'utf-8')
subject = 'Python SMTP Mail Report'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

fp = open('chart1.png', 'rb')
msgImage1 = MIMEImage(fp.read())
fp.close()
fp = open('chart2.png', 'rb')
msgImage2 = MIMEImage(fp.read())
fp.close()

msgImage1.add_header('Content-ID', '<image1>')
msgImage2.add_header('Content-ID', '<image2>')
mailMsg = """
<p>Python SMTP Mail Report</p>
<p><a href="http://www.google.com">The link to Google</a></p>
<p>The Chart：</p>
<p><img src="cid:image1"></p>
<p><img src="cid:image2"></p>
"""
msgAlternative.attach(MIMEText(mailMsg, 'html', 'utf-8'))
msgRoot.attach(msgImage1)
msgRoot.attach(msgImage2)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mailHost, 25)
    smtpObj.login(mailUser,mailPass)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print "Success"
except smtplib.SMTPException as e:
    print "Error: ", e
