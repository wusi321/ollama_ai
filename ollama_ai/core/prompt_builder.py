# core/prompt_builder.py
# 用于构建与 Ollama 模型交互的提示（Prompt）
# 所有与模型对话的文本模板都集中在这里统一管理

class PromptBuilder:
    """Prompt 构造器，生成不同类型任务的提示文本"""

    @staticmethod
    def code_analysis(code: str, language: str = "") -> str:
        """
        构造代码分析任务的 Prompt。
        :param code: 源代码字符串
        :param language: 编程语言（可选）
        """
        lang = language or "代码"
        return (
            f"你是一名经验丰富的嵌入式与系统程序员。\n"
            f"请阅读以下{lang}内容，并完成以下任务：\n"
            f"1. 简要说明这段代码的主要功能。\n"
            f"2. 分析潜在的逻辑或安全问题。\n"
            f"3. 提出可以改进的方向或优化建议。\n\n"
            f"以下是代码内容：\n"
            f"```{language}\n{code}\n```"
        )

    @staticmethod
    def image_analysis() -> str:
        """
        构造图片分析任务的 Prompt。
        """
        return (
            "你是一名计算机视觉与电子系统专家。\n"
            "请从技术和工程角度描述这张图片的内容，"
            "如果图片涉及硬件、电路或设备，请推测它的作用与结构。"
        )

    @staticmethod
    def chat_prompt(text: str) -> str:
        """
        通用聊天提示（直接返回用户输入）
        """
        return text