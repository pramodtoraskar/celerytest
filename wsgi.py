from flask import Flask
from celery import Celery

application = Flask(__name__)

BROKER_URL = 'amqp://guest:guest@rabbitmq:5672'
BACKEND_PROTOCOL = 'rpc://'

CELERY_APP = Celery('celery_task', broker=BROKER_URL, backend=BACKEND_PROTOCOL)

@application.route("/celerytest")
def celerytest():
    res = CELERY_APP.send_task('dwm_task.dwm_post_process', ('Test_Batch_ID',))
    return "Task Submitted Successfully!"

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
