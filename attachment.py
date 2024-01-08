import email.encoders
import smtplib
import mimetypes
from email.message import EmailMessage
from tkinter import filedialog
import os

message = EmailMessage()
sender = "aivademoemail@gmail.com"
recipient = "ambaliyadhruv123@gmail.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Learning to send email from medium.com'
body = """Hello I am learning to send emails using Python!!!"""
message.set_content(body)

open_file = filedialog.askopenfilename(initialdir="C:\\", )

# file name with extension
file_name = os.path.basename(open_file)

# file name without extension
# print(os.path.splitext(file_name)[0])
from pathlib import Path

# file_name = Path(open_file).stem
mime_type, _ = mimetypes.guess_type(open_file)
mime_type, mime_subtype = mime_type.split('/')
with open(open_file, 'rb') as file:
    message.add_attachment(file.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=file_name)

print(message)
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.login("aivademoemail@gmail.com", 'pjytfyzigbaqlehg')
mail_server.send_message(message)
mail_server.quit()
