import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY_TEAMSPEAK = os.getenv("API_KEY_TEAMSPEAK")

ADDRESS_SERVER = "http://156.67.63.180:10080/1/serverlist"

def status_server():
    headers = {
        "x-api-key": f"{API_KEY_TEAMSPEAK}"
    }

    response = requests.post(ADDRESS_SERVER, headers=headers)

    return response.json()["body"][0]["virtualserver_status"]
