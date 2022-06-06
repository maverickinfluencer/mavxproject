from services.googlesheets.GoogleSheetsService import GoogleSheetsService

def get_brand_info(brand_name):
    google_sheet_service = GoogleSheetsService()
    result = google_sheet_service.get_brand_info()
    for item in result:
        if item[0] == brand_name:
            print("brand_name matched")
            return tuple(item)
    return []
