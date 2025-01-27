from pass_bot import API_KEY_DEEPSEEK
import requests

URL_DEEPSEEK = "https://api.deepseek.com/v1/chat/completions"



def api_request(request):
    headers = {
        "Authorization": f"Bearer {API_KEY_DEEPSEEK}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",  # Укажи нужную модель
        "messages": [
            {"role": "user", "content": f"{request}"}
        ]
    }

    response = requests.post(URL_DEEPSEEK, json=data, headers=headers)

    return response
