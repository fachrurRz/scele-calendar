from apscheduler.schedulers.blocking import BlockingScheduler
from automation import update_trello

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=30)
def timed_job():
    print('This job is to update scele')
    update_trello()
    
sched.start()