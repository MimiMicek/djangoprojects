from celery import Celery
import yagmail
app = Celery()
app.config_from_object('celeryconfig')

receiver = "email@gmail.com"
body = "Congratulations, you are now a part of Social Network. Your life is officially over"


yag = yagmail.SMTP("email@gmail.com")
yag.send(
    to=receiver,
    subject="Signup confirmation for Social Network",
    contents=body
)