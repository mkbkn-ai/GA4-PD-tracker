import requests
import os

PIPEDRIVE_API_TOKEN = os.getenv('PIPEDRIVE_API_TOKEN')
PIPEDRIVE_API_URL = "https://api.pipedrive.com/v1/persons"

def send_to_pipedrive(data):
    payload = {
        "name": data.get('name'),
        "email": data.get('email'),
        "visible_to": 3,
        "utm_source": data.get('utm_source'),
        "utm_medium": data.get('utm_medium'),
        "utm_campaign": data.get('utm_campaign'),
        "gclid": data.get('gclid')
    }
    response = requests.post(f"{PIPEDRIVE_API_URL}?api_token={PIPEDRIVE_API_TOKEN}", json=payload)
    return response.status_code == 201
