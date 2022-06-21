from flask import Flask, jsonify, request
from datetime import datetime
from services.descriptionGenerator.PriceInfo import price_info
from flask_cors import CORS, cross_origin
from services.googlesheets.GoogleSheetsService import GoogleSheetsService
from apscheduler.schedulers.background import BackgroundScheduler
from services.descriptionGenerator.BrandDetail import get_brand_info
import atexit
from services.descriptionGenerator.GenerateDescription import get_description
from services.videodata.VideoDataService import VideoDataService
from services.web_scraping.Coupon_Code_Validator import coupon_code_validator

app = Flask(__name__)
# crontab = Crontab(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

video_data_response = {
    'last_run': "",
    'video_data_status': ""
}


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
    discount = int(req.get('discount'))
    links = req.get('product_links')
    result = price_info(links=links, discount=discount)
    return jsonify(result)


@app.route('/api/v1/admin/description', methods=['POST'])
@cross_origin()
def get_descriptions():
    req = request.json
    print("request")
    influencer_name = req.get('influencer_name')
    discount = int(req.get('discount'))
    coupon_code = req.get('coupon_code')
    campaign_month = req.get('campaign_month')
    brand_name = req.get('brand_name')
    links = req.get('product_links')
    result = get_description(influencer_name=influencer_name, discount=discount, coupon_code=coupon_code,
                             campaign_month=campaign_month, brand_name=brand_name, links=links)
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
    return "Successfully ran Video-Data_v1."


@app.route('/api/v1/admin/video-data/status', methods=['GET'])
@cross_origin()
def get_status_video_data():
    print("get_video_data_status triggered.")
    return video_data_response


@app.route('/api/v1/admin/coupon-code-status', methods=['POST'])
@cross_origin()
def get_coupon_code_status():
    req = request.json
    print(req)
    coupon_code = req.get('coupon_code')
    links = req.get('product_links')
    url = links[0]
    result = coupon_code_validator(coupon_code=coupon_code, url=url)
    return jsonify(result)


@app.route('/history')
@cross_origin()
def get_bitly_link_clicks():
    obj = GoogleSheetsService()
    return jsonify(obj.get_historical_bitly_links())


# @app.route('/scrap')
# def get_influencer_details():
#     mhs()
#     return "done"

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(generate_video_data, 'cron', hour=0, minute=0)
atexit.register(lambda: scheduler.shutdown())
if __name__ == '__main__':
    app.run(debug=True)
