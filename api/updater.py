from apscheduler.schedulers.background import BackgroundScheduler
from .job import *

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(syncdbtopstories, 'interval', minutes=5)
    scheduler.start()