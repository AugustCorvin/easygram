import requests



class TelegramAPI:
    def __init__(self, token: str):
        self.base_url = f"https:api.telegram.org/bot{token}"

    def request(self, method: str, params: dict | None = None) -> dict:
        url = f"{self.base_url}/{method}"
        response = request.post(url, json=params)
        return response.json()