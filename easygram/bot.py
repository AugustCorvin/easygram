from .api import TelegramAPI



class Bot:
    def __init__(self, token: str):
        self.api = TelegramAPI(token)
        self.offset = 0

    def send_message(self, chat_id: int, text: str):
        return self.api.request(
            "sendMessage",
            {
                "chat_id": chat_id,
                "text": text,
            },
        )

    def get_updates(self):
        data = self.api.request(
            "getUpdates",
            {"offset": self.offset + 1},
        )

        if not data.get("ok"):
            return []

        updates = data["result"]

        if updates:
            self.offset = updates[-1]["update_id"]

        return updates