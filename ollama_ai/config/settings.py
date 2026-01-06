# Ollama 服务地址（一般不用改）
OLLAMA_HOST = "http://127.0.0.1:11434"

# 文本模型
TEXT_MODEL = "gpt-oss:120b-cloud"

# 多模态模型
VISION_MODEL = "qwen3-vl:2b"

# 通用推理参数
DEFAULT_OPTIONS = {
    "temperature": 0.2,
    "top_p": 0.9,
}

# 文本切分长度
MAX_CHUNK_SIZE = 3000