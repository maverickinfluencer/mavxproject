from services.bitly.BitlyService import BitlyService
import json
import requests
from datetime import datetime, timedelta
import re
from services.time.current_time import get_current_time
from services.googlesheets.GoogleSheetsService import GoogleSheetsService

KEY = "AIzaSyD3jah3H6DjJXM9wX2KY05RNYnmD5IXgY4"


def fetch_links_from_description(description,video_id,published_at):
    # (datetime.strptime(published_at, "%d-%m-%Y %H:%M:%S") + timedelta(days=30)) == get_current_time()
    # if( abs((datetime.strptime(get_current_time(),"%d-%m-%Y %H:%M:%S") - datetime.strptime(published_at, "%d-%m-%Y")).days) < 30 ):
        bitly_links = re.findall(r'(https?://fash.la\S+)', description)
        print(bitly_links)
        print(f"fetched Bitly Links.: {bitly_links}")
        unique_bitly_links = []
        for link in bitly_links:
            if link not in unique_bitly_links:
                unique_bitly_links.append(link)
        print(f"unique bitly links {unique_bitly_links}")
        bitly_service = BitlyService()
        return bitly_service.fetch_bitly_link_clicks(links=unique_bitly_links,video_id=video_id)
    # elif():
    #     # upload date greater than 30 but less than 60
    #     return
    # else:
    #     # currently getting videosIds which are less than 60 days
    #     return

class YouTubeService:
    def get_metrics(self, video_id):
        vid_link=""
        vid_date=""
        vid_title=""
        channel_id=""
        temp_list=""
        expected_views=0
        vid_views=0
        vid_likes=0
        vid_comments=0
        sum_of_link_cliks=0
        failed_link_list=[]
        final_bitly_status=False
        google_sheet_service = GoogleSheetsService()
        youtube_status = False
        bitly_status = False
        description = ''
        videoLink = f"https://www.youtube.com/watch?v={video_id}"
        try:
            url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={KEY}&part=snippet,statistics"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            print(f'data: {data}')
            temp_list = []
            youtube_list = []
            # yt_updated_at = get_current_time()
            for i in data['items']:
                vid_link = 'https://www.youtube.com/watch?v=' + i.get('id')
                # playtime = i['contentDetails'].get('duration')
                # vid_runtime = isodate.parse_duration(playtime).total_seconds()
                vid_title = i['snippet'].get('title')
                channel_id = i['snippet'].get('channelId')
                description = i['snippet'].get('description')
                # channel_title = i['snippet'].get('channelTitle')
                vid_date = i['snippet'].get('publishedAt')[:10]
                vid_views = i['statistics'].get('viewCount')
                vid_likes = i['statistics'].get('likeCount')
                vid_comments = i['statistics'].get('commentCount')
                expected_views = 0
                youtube_status = True
            youtube_list.append((
                video_id, vid_link, vid_date, channel_id, vid_title, expected_views, vid_views, vid_likes,
                vid_comments, get_current_time(), youtube_status
            ))
            print(youtube_list)
            # upload it to final output Spread Sheet
            print("youtube metrics uploading to Historical data v1")
            google_sheet_service.add_row(model=youtube_list, tab_range='Youtube',spread_sheet_id='1hq-i4YKAGv7HvirtjqL-8TNOH0RPHXUTqyFy8oOLSFE')
            print("Youtube metrics added to Historical data.")
        except:
            youtube_status = False
        finally:
            if len(description) != 0:
                sum_of_link_cliks, failed_link_list, final_bitly_status = fetch_links_from_description(description=description,video_id=video_id, published_at=vid_date)
            temp_list.append((
                video_id, vid_link, vid_date, channel_id, vid_title, expected_views, vid_views, vid_likes, vid_comments,
                sum_of_link_cliks, get_current_time(), final_bitly_status, youtube_status
            ))
            print("uploading metrics to Today video data v1")
            google_sheet_service.add_row(model=temp_list, tab_range="output",
                                         spread_sheet_id='1pCI31UUBQtMJiH2mAqjeC3siE0Pks3yu1xRupS8a9QY')
        print("done")
