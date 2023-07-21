import smtplib, ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'youremail@gmail.com'
    password = 'mailpassword'

    receiver = 'youremail@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    # with smtplib.SMTP("smtp.gmail.com") as server:
    #     server.starttls() and server.login(user=username, password=password)
    #     server.sendmail(from_addr=username,
    #                     to_addrs=receiver,
    #                     msg=message)