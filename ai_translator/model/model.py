from book import ContentType


class Model:
    def make_text_prompt(self, text: str, target_language: str) -> str:
        return f"以下文本翻译为{target_language}：\n{text}"

    def make_line_prompt(self, text: str, target_language: str) -> str:
        return f"以下文本翻译为{target_language}：\n{text}"

    def make_table_prompt(self, table: str, target_language: str) -> str:
        return f"以下文本{table}翻译为{target_language}，翻译内容续保持间距（空格，分隔符），以表格形式返回."

    def translate_prompt(self, content, target_language: str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, target_language)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), target_language)
        elif content.content_type == ContentType.TEXTLINE:
            return self.make_line_prompt(content.get_original_as_str(), target_language)

    def make_request(self, prompt):
        raise NotImplementedError("子类必须实现 make_request 方法")
