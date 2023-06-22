import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailSender:

    def __init__(self, mail, password):
        # Sender credentials
        self.mail = mail
        self.password = password

    def send(self, receiver, message):
        # Email content
        msg = MIMEMultipart("alternative")
        msg["From"] = self.mail
        msg["To"] = receiver

        msg["Subject"] = "Ανακοίνωση Τμήματος Ηλεκτρολόγων και Ηλεκτρονικών Μηχανικών"

        # Combine header, main text, and footer with HTML formatting
        email_content = message

        # Attach the email content as HTML
        msg.attach(MIMEText(email_content, "html"))
        msg.attach(MIMEText(email_content.get_text(), "plain"))

        # Create a secure SSL/TLS connection to the SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            # Log in to your Gmail account
            server.login(self.mail, self.password)

            # Send the email
            server.send_message(msg)
