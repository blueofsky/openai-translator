from langchain_openai import ChatOpenAI

from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

import os
from book import Content,ContentType
from utils import LOG
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

class TranslationChain:
    def __init__(self, model_type: str = "openai",model_name: str = "gpt-3.5-turbo", verbose: bool = True):
        chat_prompt_template = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                """
                    将输入的文本从 {source_language} 翻译为 {target_language} {specification}.
                """
            ),
            HumanMessagePromptTemplate.from_template("{text}")
        ])

        if model_type == "openai":
            chat = ChatOpenAI(model_name=model_name, temperature=0, verbose=verbose)
        else:            
            chat = ChatOllama(base_url=os.getenv("OLLAMA_API_BASE") or "http://localhost:11434",model=model_name,temperature=0, verbose=verbose)

        self.chain=chat_prompt_template|chat|StrOutputParser()

    def run(self, content: Content, source_language: str, target_language: str):
        result = ""
        try:
            text=""
            specification=""
            if content.content_type == ContentType.TEXT:
                text=content.original                
            elif content.content_type == ContentType.TABLE:
                text=content.get_original_as_str()
                specification="，翻译内容续保持间距（空格，分隔符），以表格形式返回"
            elif content.content_type == ContentType.TEXTLINE:
                text=content.get_original_as_str()
            
            result = self.chain.invoke({
                "text": text,
                "specification": specification,
                "source_language": source_language,
                "target_language": target_language,
            })
        except Exception as e:
            LOG.error(f"An error occurred during translation: {e}")
            return result, False

        return result, True