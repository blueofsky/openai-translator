import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser
from model import ModelConfig
from translator import PDFTranslator

if __name__ == "__main__":
    config = ModelConfig(ArgumentParser().parse_arguments())
    translator = PDFTranslator(config.model)
    translator.translate_pdf(config.pdf_file_path, config.file_format, config.language)
