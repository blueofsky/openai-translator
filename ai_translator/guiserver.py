import os
import sys

import gradio as gr
from model import ModelConfig
from translator import PDFTranslator
from utils import LOG, ArgumentParser

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# 函数：翻译文件内容
# 参数：
#   input_file: 待翻译文件
#   target_language: 目标语言
#   file_format: 目标文件格式
def translation(input_file, target_language, file_format):
    # 判断参数是否为空
    if not input_file or not target_language or not file_format:
        return "参数不能为空"
    LOG.debug(f"[翻译任务]\n源文件: {input_file.name}\n目标语言: {target_language}\n目标文件格式: {file_format}")
    translator = PDFTranslator(model)
    return translator.translate_pdf(pdf_file_path=input_file, file_format=file_format, target_language=target_language)


if __name__ == "__main__":
    model = ModelConfig(ArgumentParser().parse_arguments()).model
    iface = gr.Interface(
        fn=translation,
        title="PDF电子书翻译工具",
        inputs=[
            gr.File(label="源文件(PDF格式)", type="filepath"),
            gr.Dropdown(label="目标语言", choices=["中文", "日语", "法语", "德语"], allow_custom_value=True),
            gr.Dropdown(label="目标文件格式", choices=[("PDF", "pdf"), ("Markdown", "markdown")])
        ],
        outputs=[
            gr.File(label="翻译文件(可下载)")
        ],
        allow_flagging="never"
    )
    iface.launch()
