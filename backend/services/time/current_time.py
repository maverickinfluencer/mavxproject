from datetime import datetime


def get_current_time():
    current_time = datetime.now()
    return current_time.strftime("%d-%m-%Y %H:%M:%S")
