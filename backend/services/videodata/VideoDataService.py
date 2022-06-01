import time

from services.googlesheets.GoogleSheetsService import GoogleSheetsService
from services.youtube.YouTubeService import YouTubeService


class VideoDataService:
    def generate_video_data(self):
        print('generate_video_data triggered.')
        google_sheets_service = GoogleSheetsService()
        # fetch video ids from Google sheets
        list_video_ids = google_sheets_service.get_video_ids_from_google_sheets()
        # empty google sheets
        response = google_sheets_service.empyt_sheet()
        # print(f'response from google sheets empty method: {response}')
        # fetch metrics from YouTube
        youtube_service = YouTubeService()
        for video_id in list_video_ids:
            time.sleep(5)
            youtube_service.get_metrics(video_id=video_id)
        print("Done")
