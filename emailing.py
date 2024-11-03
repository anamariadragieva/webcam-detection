import smtplib
import filetype
from email.message import EmailMessage

PASSWORD = "vzdjlnsyjdropumx"
SENDER = "amyyoo98@gmail.com"
RECEIVER = "krisaka950311@gmail.com"


def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New Movement Detected"
    email_message.set_content("Hey, there's been a movement detected on your desktop camera!")

    with open(image_path, 'rb') as file: #using 'rb' - read in binary mode
        content = file.read()
    kind = filetype.guess(image_path)
    email_message.add_attachment(content, maintype="image", subtype=kind.mime.split('/')[1])

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/19.png")

