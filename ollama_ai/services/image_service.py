from core.ollama_client import OllamaClient
from core.prompt_builder import PromptBuilder
from config.settings import VISION_MODEL

class ImageService:
    def __init__(self):
        self.client = OllamaClient(VISION_MODEL)

    def analyze(self, image_path: str):
        prompt = PromptBuilder.image_analysis()
        return self.client.chat(
            messages=[{"role": "user", "content": prompt}],
            images=[image_path]
        )