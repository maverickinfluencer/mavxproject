from flask import Flask
from services.videodata.VideoDataService import VideoDataService
from flask_crontab import Crontab
app = Flask(__name__)
crontab = Crontab(app)

@app.route('/')
def hello_world():  # put application's code here
    print("hello world function called.")
    print("newly add")
    return 'Hello World!'

@app.route('/api/v1/admin/video-data')
def generate_video_data():
    print("generate_video_data controller triggered.")
    obj = VideoDataService()
    obj.generate_video_data()
    return "DONE"


if __name__ == '__main__':
    app.run()
