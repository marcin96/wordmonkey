#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import smtplib
from email.mime.text import MIMEText

def sendMail(logfilename,mail):
    '''
    If the Prozess is finished this
    method sends a mail with the log file
    as Context to the given mail adress.
    '''
    with open(logfilename) as fp:
        msg = MIMEText(fp.read())
    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = ""
    msg['To'] = mail
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
