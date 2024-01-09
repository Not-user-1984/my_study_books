import smtplib
# Вот пример отправки электронного письма:
sender_email = "example@gmail.com"
receiver_email = "recipient@example.com"
password = "mypassword"

message = """\
Subject: Hi there

This is an example email sent with Python."""
# SMTP расшифровывается как Simple Mail Transfer Protocol (Простой Протокол передачи почты)
# и является стандартным протоколом для отправки электронной почты через интернет.
# Он используется для отправки писем от одного сервера электронной почты к другому,
# а также для отправки писем от почтовых клиентов (например, Microsoft Outlook или Gmail)
# к серверам электронной почты.
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

 #   А вот пример получения электронного письма:
import imaplib

username = "example@gmail.com"
password = "mypassword"
# IMAP4 расшифровывается как Internet Message Access Protocol version 4
# (Протокол доступа к сообщениям электронной почты через интернет, версия 4) 
# и является протоколом для получения электронной почты с удаленного сервера.
# Он позволяет пользователям организовать свою электронную почту на сервере,
# не загружая все письма на локальный компьютер.
with imaplib.IMAP4_SSL("imap.gmail.com") as mail:
    mail.login(username, password)
    mail.select("inbox")

    _, search_data = mail.search(None, "ALL")
    for num in search_data[0].split():
        _, msg_data = mail.fetch(num, "(RFC822)")
        print(msg_data[0][1])


#   А вот пример получения электронного письма по pop3 очень древний говарят сам цезарь придумал:
import poplib

# POP3 расшифровывается как Post Office Protocol version 3
# (Протокол почтового отделения, версия 3) и является протоколом для получения электронной почты 
# с удаленного сервера.
# Он позволяет пользователям загружать все свои письма на локальный компьютер или устройство,
# что может быть полезно, если у вас нет надежного и быстрого подключения к Интернету.
server = poplib.POP3('example.com')
server.user('username')
server.pass_('password')

# Получаем список писем на сервере
messages_count = len(server.list()[1])
print(f"Found {messages_count} messages on the server")

# Получаем информацию о первых 10 письмах
for i in range(1, 11):
    response, lines, octets = server.top(i, 0)
    print(f"Message {i}: {lines}")