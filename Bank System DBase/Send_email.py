import smtplib
import ssl
from email.mime.text import MIMEText


class Bank_email:
    def __init__(self):
        self.from_email = "michaelsmtp1@gmail.com"
        self.from_password = ""

    def create_account_email(self, name, email, account_no, pin):
        to_email = email

        subject = "Your information for Bank_system"
        message = """
        <h3>Thank you for using Bank_system</h3>\n
        <h4>Here your information</h4>
        <p>Name: <strong>%s</strong></p>
        <p>Account No: <strong>%s</strong></p>
        <p>Pin: <strong>%s</strong></p>
        """ % (name, account_no, pin)

        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = self.from_email

    def deposit_email(self):
        pass

    def email_login(self):
        context = ssl.create_default_context()

        try:
            gmail = smtplib.SMTP("smtp.gmail.com", 587)
            gmail.ehlo()
            gmail.starttls(context= context)
            gmail.login(self.from_email, from_password)
            gmail.send_message(msg)
        except Exception as e:
            return e
        finally:
            gmail.quit()
