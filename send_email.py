from email.mime.text import MIMEText
import smtplib

def send_email(email, height,average_height):
    from_email = "haveagoodday965@gmail.com"
    from_password = "Aa893260110"
    to_email = email

    subject = "Height data is here"
    message = "Hey! You height data is <strong>%s</strong> cm. The average is <strong>%s</strong> cm. Don't tell anyone else!" % (height,average_height) 
    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)