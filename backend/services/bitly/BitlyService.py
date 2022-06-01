from urllib.parse import urlparse
import requests
import json
from datetime import datetime
from services.googlesheets.GoogleSheetsService import GoogleSheetsService
link_count_headers = {'Authorization': 'Bearer 62bc203ade942dba3a485c965fb69a3f01cace1f'}
link_expanded_headers = {'Authorization': 'Bearer 62bc203ade942dba3a485c965fb69a3f01cace1f',
                         'Content-Type': 'application/json'}


class BitlyService:
    def fetch_bitly_link_clicks(self, links, video_id):
        final_bitly_status = False
        status = False
        click_count_list = []
        failed_link_list = []
        click = 0
        for link in links:
            if 'fash.la' in link:
                bitly_link_list = []
                try:
                    parsed = urlparse(link)
                    _url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary?units=-1'.format(
                        parsed.netloc + parsed.path)
                    click = int(json.loads(requests.get(_url, headers=link_count_headers).text)['total_clicks'])
                    click_count_list.append(click)
                    status = True
                except :
                    status = False
                    failed_link_list.append(link)
                print(f'linkCount: {click_count_list}')
                current_date_time = datetime.now()
                updated_at = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
                bitly_link_list.append((
                    video_id, link, click, updated_at, status
                ))
                google_sheet_service = GoogleSheetsService()
                google_sheet_service.add_row(model=bitly_link_list,tab_range='Link',spread_sheet_id='1hq-i4YKAGv7HvirtjqL-8TNOH0RPHXUTqyFy8oOLSFE')
        if(len(failed_link_list) == 0):
            final_bitly_status = True
        return sum(click_count_list),failed_link_list,final_bitly_status