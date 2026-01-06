from core.ollama_client import OllamaClient
from core.prompt_builder import PromptBuilder
from utils.file_loader import read_file
from config.settings import TEXT_MODEL

class CodeService:
    def __init__(self):
        self.client = OllamaClient(TEXT_MODEL)

    def analyze_file(self, file_path: str):
        code = read_file(file_path)
        prompt = PromptBuilder.code_analysis(code)
        return self.client.chat([
            {"role": "user", "content": prompt}
        ])