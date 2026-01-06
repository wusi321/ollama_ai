import ollama
from config.settings import DEFAULT_OPTIONS
from utils.logger import get_logger

logger = get_logger("OllamaClient")

class OllamaClient:
    def __init__(self, model: str):
        self.model = model
        logger.info(f"Using model: {model}")

    def chat(self, messages, images=None, options=None):
        payload = {
            "model": self.model,
            "messages": messages,
            "options": options or DEFAULT_OPTIONS,
        }

        if images:
            payload["messages"][0]["images"] = images

        response = ollama.chat(**payload)
        return response["message"]["content"]