from core.ollama_client import OllamaClient
from config.settings import TEXT_MODEL

class ChatService:
    def __init__(self):
        self.client = OllamaClient(TEXT_MODEL)

    def chat(self, text: str):
        return self.client.chat([
            {"role": "user", "content": text}
        ])