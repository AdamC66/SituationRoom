from situationroom.celery import app
import logging
import time
# Get an instance of a logger
logger = logging.getLogger(__name__)
@app.task
def heartbeat(text="thump"):
    string = f'heartbeat: {text}'
    logger.info(string)
    time.sleep(3)
    return string
