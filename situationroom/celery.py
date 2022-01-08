import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'situationroom.settings')

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from situationroom.tasks.tasks import heartbeat
    sender.add_periodic_task(
        crontab(minute="*"),
        heartbeat.s("One minute heartbeat"),
        name="Heartbeat every minute",
    )
