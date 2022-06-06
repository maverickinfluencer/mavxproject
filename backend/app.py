from flask import Flask, jsonify, request
from datetime import datetime
from services.descriptionGenerator.PriceInfo import price_info
from flask_cors import CORS, cross_origin

from services.descriptionGenerator.BrandDetail import get_brand_info

from services.videodata.VideoDataService import VideoDataService
from flask_crontab import Crontab
from models.video_data_v1.videoDataStatus import video_data_response

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
crontab = Crontab(app)


@app.route('/')
def hello_world():  # put application's code here
    print("hello world function called.")
    print("newly add")
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
    return "DONE"


@app.route('/api/v1/admin/video-data/status', methods=['GET'])
@cross_origin()
def get_status_video_data():
    print("get_video_data_status triggered.")
    return video_data_response


if __name__ == '__main__':
    app.run()
