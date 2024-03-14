import smtplib, ssl

host = "smtp.gmail.com"
port = 465


def send_email(message):
    username = "samyorangy1@gmail.com"
    password = "rwovfcoibzpxungw"
    receiver = "samyorangy1@gmail.com"
    context =  ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)