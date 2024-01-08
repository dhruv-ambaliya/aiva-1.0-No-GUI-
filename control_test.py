import smtplib
import time
import imaplib
import email
import traceback 
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
# ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "aivademoemail@gmail.com"
FROM_PWD = "pjytfyzigbaqlehg"
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993



def get_email_body(self,msg):
        "Parse out the text of the email message. Handle multipart messages"
        email_body = []
        maintype = msg.get_content_maintype()
        if maintype == 'multipart':
            for part in msg.get_payload():
                if part.get_content_maintype() == 'text':
                    email_body.append(part.get_payload())
        elif maintype == 'text':
            email_body.append(msg.get_payload())

        return email_body


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')
                    get_email_body(msg)

    except Exception as e:
        traceback.print_exc() 
        print(str(e))

read_email_from_gmail()