ollama_ai/
├── README.md
├── requirements.txt           #requirements.txt
├── main.py                  # 程序入口
│
├── config/
│   ├── __init__.py
│   └── settings.py          # 模型名、参数、路径等
│
├── core/
│   ├── __init__.py
│   ├── ollama_client.py     # Ollama 通信封装（核心）
│   └── prompt_builder.py    # Prompt 构造逻辑
│
├── services/
│   ├── __init__.py
│   ├── code_service.py      # 代码分析
│   ├── image_service.py     # 图片分析
│   └── chat_service.py      # 纯对话
│
├── utils/
│   ├── __init__.py
│   ├── file_loader.py       # 读文件、读工程
│   ├── logger.py
│   └── text_splitter.py     # 长文本切分
│
├── data/
│   ├── sample_code.c
│   └── board.jpg
│
└── tests/
    └── test_code_service.py