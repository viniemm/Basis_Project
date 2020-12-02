import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
import pandas as pd
import yagmail
import os


def mail(address: str, filename: str):
    receiver = address
    body = "Your portfolio is attached as a csv file. Open in google sheets to track"
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, filename)
    df = pd.read_csv(my_file)
    col = list()
    for x in range(1, len(df)+1):
        col.append("=GOOGLEFINANCE(A"+str(x+1)+", \"PRICE\")")
    df.insert(1, "cmp", col)
    df.to_csv(my_file, index=False)
    try:
        yag = yagmail.SMTP("vinipy2020@gmail.com")
        yag.send(
            to=receiver,
            subject="BASIS Project Stock Report",
            contents=body,
            attachments=my_file,
        )
    except yagmail.error.YagInvalidEmailAddress:
        print("Invalid Email")
    df = pd.read_csv(my_file)
    df = df.drop(["cmp"], axis=1)
    df.to_csv(my_file, index=False)





def old_mail(address: str, filename: str):
    password = getpass("Key: ")
    port = 465  # For SSL

    sender_email = "vinipy2020@gmail.com"
    receiver_email = address
    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email
    message.attach(MIMEText(body, "plain"))

    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("vinipy2020@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)
