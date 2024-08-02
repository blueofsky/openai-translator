import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, LOG
from translator import PDFTranslator, TranslationConfig
from server import launch_api_server, launch_gradio_server

def launch_cmd():
    translator = PDFTranslator(config.model_type,config.model_name)
    translator.translate_pdf(config.input_file,
                             config.source_language,
                             config.target_language,
                             config.target_file_format)

if __name__ == "__main__":
    command,args = ArgumentParser().parse_arguments()
    if command:
        config = TranslationConfig()
        config.initialize(args)

        if command == 'apiserver':
            launch_api_server(config.model_type,config.model_name)
        elif command == 'gradio':
            launch_gradio_server(config.model_type,config.model_name)
        else:
            launch_cmd()
