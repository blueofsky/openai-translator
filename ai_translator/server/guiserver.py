import gradio as gr
from translator import PDFTranslator
from utils import LOG

def translation(input_file, source_language, target_language,target_file_format):
    LOG.debug(f"[翻译任务]\n源文件: {input_file.name}\n源语言: {source_language}\n目标语言: {target_language}")

    output_file_path = Translator.translate_pdf(input_file, 
                                                source_language, target_language,target_file_format)

    return output_file_path

def launch_gradio_server(model_type,model_name):
    global Translator
    Translator = PDFTranslator(model_type,model_name)
    iface = gr.Interface(
        fn=translation,
        title="OpenAI-Translator v2.0（PDF 电子书翻译工具）",
        inputs=[
            gr.File(label="上传PDF文件", type="filepath"),
            gr.Dropdown(label="源语言（默认：英文）", value="英文",choices=["英文", "中文"], allow_custom_value=True),
            gr.Dropdown(label="目标语言（默认：中文）", value="中文",choices=["英文", "中文"], allow_custom_value=True),
            gr.Dropdown(label="目标文件格式", value="markdown",choices=[("PDF", "pdf"), ("Markdown", "markdown")]),
        ],
        outputs=[
            gr.File(label="下载翻译文件")
        ],
        allow_flagging="never"
    )
    iface.launch(share=True, server_name="0.0.0.0")