import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver_email):
    port = 465  # For SSL
    # Create a secure SSL context

    sender_email = "rasachatbot00@gmail.com"
    message = """\
    Subject: Hi there\

    This is an automated message from the Zaka Chatbot.
    You are now subscribed to our newsletter, {name}!"""

    # Send email here
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("rasachatbot00@gmail.com", "Roze@Zaka.ai")
        server.sendmail(sender_email, receiver_email, message.format(name="Person"))

    print('Email was sent!')

def send_program_email(email, name, age, phone, occupation, topic):
    port = 465  # For SSL
    # Create a secure SSL context

    sender_email = "rasachatbot00@gmail.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Thank you for subscribing!"
    message["From"] = sender_email
    message["To"] = email
    # write the plain text part
    text = "Hi, {name}! \nThank you for subscribing to the {topic} program! Here is a receipt with the subscription details: \nAge: {age} \nExperience Level: {occupation} \nPhone Number: {phone} \nPrice: $ 99.99".format(name=name, occupation=str(occupation), age=str(age), phone=str(phone), topic=topic)
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi {name},<br>
          Thank you for subscribing to the {occupation} program. We look forward to having you. Please note below a receipt of your details:</p>
        <p>Age: {age}</p>
        <p>Length of Experience: {occupation}</p>
        <p>Phone: {phone}</p>
        <p>Topic: {topic}</p>
      </body>
    </html>
    """.format(name=name, occupation=str(occupation), age=str(age), phone=str(phone), topic=topic)

    # convert both parts to MIMEText objects and add them to the MIMEMultipart message
    part1 = MIMEText(html, 'html')
    part2 = MIMEText(text, "plain")
    message.attach(part1)
    message.attach(part2)

    # Send email here
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("rasachatbot00@gmail.com", "Roze@Zaka.ai")
        server.sendmail(sender_email, email, message.as_string())

    print('Email was sent!')