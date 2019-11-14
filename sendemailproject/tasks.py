# from celery import Celery
# import yagmail
# # app = Celery(
# #     'tasks',
# #     backend='redis://localhost',
# #     broker='redis://localhost'
# #     )
#
# app = Celery()
# app.config_from_object('celeryconfig')
#
# # @app.task
# # def add(x, y):
# #     return x + y
#
# receiver = "micekpython@gmail.com"
# body = "Hello there from KEA"
# #filename = "document.pdf"
#
# yag = yagmail.SMTP("micekpython@gmail.com")
# yag.send(
#     to=receiver,
#     subject="Yagmail test with attachment",
#     contents=body,
#     #attachments=filename,
# )