from apscheduler.schedulers.background import BackgroundScheduler
from services.videodata.VideoDataService import VideoDataService
import time
scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()
video_data_service = VideoDataService()
job = scheduler.add_job(video_data_service.generate_video_data(),'cron',hour="17",minute="9")
print(job)
while True:
    time.sleep(1)
