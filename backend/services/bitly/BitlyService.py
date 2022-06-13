from urllib.parse import urlparse
import requests
import json
from services.time.current_time import get_current_time
from datetime import datetime,date,timedelta
from services.googlesheets.GoogleSheetsService import GoogleSheetsService
link_count_headers = {'Authorization': 'Bearer 62bc203ade942dba3a485c965fb69a3f01cace1f'}
link_expanded_headers = {'Authorization': 'Bearer 62bc203ade942dba3a485c965fb69a3f01cace1f',
                         'Content-Type': 'application/json'}


class BitlyService:
    def fetch_bitly_link_clicks(self, links, video_id):
        google_sheet_service = GoogleSheetsService()
        # historical_links = google_sheet_service.get_historical_bitly_links()
        final_bitly_status = False
        status = False
        click_count_list = []
        failed_link_list = []
        click = 0
        second_click = 0
        for link in links:
            if 'fash.la' in link:
                # for historical_link in historical_links:
                #     if(historical_link[1] == link and (abs(datetime.strptime(get_current_time(),"%d-%m-%Y %H:%M:%S") - datetime.strptime(historical_link[3],"%d-%m-%Y %H:%M:%S")))>30):
                #     return
                bitly_link_list = []
                try:
                    parsed = urlparse(link)
                    print(parsed)
                    _url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary?units=30'.format(
                        parsed.netloc + parsed.path)
                    click = int(json.loads(requests.get(_url, headers=link_count_headers).text)['total_clicks']) or 0
                    status = True
                    current_date = date.today()
                    days = timedelta(30)
                    second_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc+parsed.path}/clicks/summary?unit=day&units=30&unit_reference={current_date-days}T00%3A00%3A00%2B0000'
                    second_click = int(json.loads(requests.get(second_url, headers=link_count_headers).text)['total_clicks']) or 0
                    print(second_click)
                    click_count_list.append(click+second_click)
                except :
                    status = False
                    failed_link_list.append(link)
                print(f'linkCount: {click_count_list}')
                # bitly_updated_at = get_current_time()
                bitly_link_list.append((
                    video_id, link, click+second_click, get_current_time(), status
                ))
                google_sheet_service.add_row(model=bitly_link_list,tab_range='Link',spread_sheet_id='1hq-i4YKAGv7HvirtjqL-8TNOH0RPHXUTqyFy8oOLSFE')
        if(len(failed_link_list) == 0):
            final_bitly_status = True
        return sum(click_count_list),failed_link_list,final_bitly_status