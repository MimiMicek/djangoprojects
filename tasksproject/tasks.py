from celery import Celery

# app = Celery(
#     'tasks',
#     backend='redis://localhost',
#     broker='redis://localhost'
#     )

app = Celery()
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y
