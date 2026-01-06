from services.code_service import CodeService
from services.image_service import ImageService
from services.chat_service import ChatService

def main():
    print("=== Chat ===")
    chat = ChatService()
    print(chat.chat("你是谁，用一句话说明"))

    print("\n=== Code Analysis ===")
    code = CodeService()
    print(code.analyze_file("data/sample_code.c"))

    print("\n=== Image Analysis ===")
    image = ImageService()
    print(image.analyze("data/board.jpeg"))

if __name__ == "__main__":
    main()