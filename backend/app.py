from flask import Flask, jsonify, request
from datetime import datetime
from services.descriptionGenerator.PriceInfo import price_info
from flask_cors import CORS, cross_origin
from services.googlesheets.GoogleSheetsService import GoogleSheetsService
from flask_apscheduler import APScheduler

from services.descriptionGenerator.BrandDetail import get_brand_info

from services.videodata.VideoDataService import VideoDataService
from models.video_data_v1.videoDataStatus import video_data_response

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def hello_world():  # put application's code here
    print("hello world function called.")
    return 'Hello World'


@app.route('/api/v1/admin/video-description/brand-info/<brand_name>', methods=['GET'])
@cross_origin()
def get_brand_detail(brand_name):
    print("get_brand_detail triggerd with brand_name= " + brand_name)
    result = get_brand_info(brand_name)
    return jsonify(result)


@app.route('/api/v1/admin/price-info', methods=['POST'])
@cross_origin()
def get_price_info():
    req = request.json
    print("request=")
    print(req)
    brand_name = req.get('brand_name')
    influencer_name = req.get('influencer_name')
    discount = int(req.get('discount'))
    links = req.get('product_links')
    result = price_info(links=links, discount=discount)
    return jsonify(result)

@app.route('/api/v1/admin/video-data')
@scheduler.task('cron', id='do_job_1', hour='00', minute='00', day='*')
def generate_video_data():
    # last_run = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    video_data_response['last_run'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    last_run = video_data_response.get('last_run')
    print(f"generate_video_data controller triggered. at {last_run} ")
    try:
        video_data_response['video_data_status'] = "RUNNING"
        obj = VideoDataService()
        obj.generate_video_data()
        video_data_response['video_data_status'] = "SUCCESS"
    except:
        video_data_response['video_data_status'] = "FAILED"
    return "Successfully ran Video-Data_v1."


@app.route('/api/v1/admin/video-data/status', methods=['GET'])
@cross_origin()
def get_status_video_data():
    print("get_video_data_status triggered.")
    return video_data_response

@app.route('/history')
@cross_origin()
def get_bitly_link_clicks():
    obj = GoogleSheetsService()
    return jsonify(obj.get_historical_bitly_links())

@scheduler.task('cron', id='do_job_2', hour='19', minute='35')
def job2():
    print('Job 2 executed')

if __name__ == '__main__':
    app.run(port=8000)
