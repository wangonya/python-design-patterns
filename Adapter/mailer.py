# NOTE: come back to this. I didn't get it, or maybe the code was wrong (it did have a lot of typos)
import smtplib
from email.mime.text import MIMEText


class UserFetcher:
    def __init__(self, users_csv_file):
        self.users_csv_file = users_csv_file

    def fetch_users(self):
        return [{"email": "user1@mail.com"}, {"email": "user2@mail.com"}]


class Mailer:
    def send(self, sender, recipients, subject, message):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = [recipients]

        # s = smtplib.SMTP("localhost")
        # s.send_message(recipients)
        # s.quit()
        print("sending message from Mailer ... ")


class Logger:
    def output(self, message):
        print(f"[Logger]: {message}")


class LoggerAdapter:
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def send(self, sender, recipients, subject, message):
        log_message = (
            f"From: {sender}\nTo: {recipients}\nSubject: {subject}\nMessage: {message}"
        )
        self.what_i_have.output(log_message)

    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)


if __name__ == "__main__":
    user_fetcher = UserFetcher("users.csv")
    mailer = Mailer()
    mailer.send(
        "me@example.com",
        [x["email"] for x in user_fetcher.fetch_users()],
        "Subject",
        "Message",
    )
