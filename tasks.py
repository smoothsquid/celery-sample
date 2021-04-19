from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

app = Celery("tasks", broker="memory://localhost/", backend="rpc://")

app.conf.update(

)

@app.task
def add(x, y):
    print("{}".format(x + y))
    return x + y

app.conf.beat_schedule = {
    "add-at-two-seconds": {
        "task": "tasks.add",
        "schedule": timedelta(seconds=1),
        "args": (15, 50),
    }
}