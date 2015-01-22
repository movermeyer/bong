import time

def run(settings, sleep=time.sleep, notify=print):
    sleep(settings.time)
    notify(settings.message)

