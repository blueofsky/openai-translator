import os
import shutil
import sys
import tempfile

import uvicorn
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import Response, JSONResponse, FileResponse

from model import ModelConfig
from translator import PDFTranslator
from utils import ArgumentParser

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 创建应用
app = FastAPI()


# 接口：上传并翻译文件
# 参数：
#   target_language: 目标语言
#   file_format: 文件格式
#   input_file: 上传的文件
# 返回：
#   翻译文件
@app.post(path='/translation', response_class=Response)
async def translation(input_file: UploadFile = File(),
                      target_language: str = Form(),
                      file_format: str = Form()):
    try:
        if input_file and input_file.filename:
            # # 创建临时文件
            input_file_path = os.path.join(tempfile.gettempdir(), input_file.filename)
            with open(input_file_path, "wb") as buffer:
                shutil.copyfileobj(input_file.file, buffer)
            # 调用翻译函数
            translator = PDFTranslator(model)
            output_file_path = translator.translate_pdf(
                pdf_file_path=input_file_path,
                file_format=file_format,
                target_language=target_language)
            filename = os.path.basename(output_file_path)
            # return {'status': 'success', 'message': '翻译成功', 'filename': filename}
            return FileResponse(path=os.path.join(tempfile.gettempdir(), filename),
                                filename=filename,
                                media_type="application/octet-stream")
    except Exception as e:
        return JSONResponse({'status': 'error', 'message': str(e)}, status_code=400)


if __name__ == '__main__':
    model = ModelConfig(ArgumentParser().parse_arguments()).model
    uvicorn.run(app, log_level="info", workers=1)
