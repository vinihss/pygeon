import smtplib
from email.mime.text import MIMEText
from .messenger import Messenger

class EmailMessenger(Messenger):
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_message(self, recipient, message):
        msg = MIMEText(message)
        msg['Subject'] = 'Mensagem do Pygeon'
        msg['From'] = self.username
        msg['To'] = recipient

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.username, recipient, msg.as_string())
