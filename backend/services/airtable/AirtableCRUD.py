import requests
import os

# AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = "Description%20and%20Price%20Info"
API_KEY = "keysC422zvQpwRs88"
headers = {
    "Authorization": "Bearer keysC422zvQpwRs88",
    "Content-Type": "application/json"
}


def update_description_airtable(record_id, description, base_id):
    AIRTABLE_ENDPOINT = f"https://api.airtable.com/v0/{base_id}/{AIRTABLE_TABLE_NAME}"
    data = {
        "records": [
            {
                "id": record_id,
                "fields": {
                    "description": description
                }
            }
        ]
    }

    r = requests.patch(AIRTABLE_ENDPOINT, json=data, headers=headers)
    print(r.json())


def update_price_info_airtable(record_id, price_info, base_id):
    AIRTABLE_ENDPOINT = f"https://api.airtable.com/v0/{base_id}/{AIRTABLE_TABLE_NAME}"
    data = {
        "records": [
            {
                "id": record_id,
                "fields": {
                    "price-information": price_info
                }
            }
        ]
    }

    r = requests.patch(AIRTABLE_ENDPOINT, json=data, headers=headers)
    print(r.json())
# print(r.json())
