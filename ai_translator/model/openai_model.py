from openai import OpenAI,RateLimitError
import requests
import simplejson
import time

from model import Model
from utils import LOG

class OpenAIModel(Model):
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.api_key = api_key

    def make_request(self, prompt):
        attempts = 0
        client = OpenAI(api_key=self.api_key)
        while attempts < 3:
            try:
                response = client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                translation = response.choices[0].message.content.strip()
                return translation, True
            except RateLimitError:
                attempts += 1
                if attempts < 3:
                    LOG.warning("Rate limit reached. Waiting for 60 seconds before retrying.")
                    time.sleep(60)
                else:
                    raise Exception("Rate limit reached. Maximum attempts exceeded.")
            except requests.exceptions.Timeout as e:
                raise Exception(f"请求超时：{e}")
            except requests.exceptions.RequestException as e:
                raise Exception(f"请求异常：{e}")
            except simplejson.JSONDecodeError as e:
                raise Exception("Error: response is not valid JSON format.")
            except Exception as e:
                raise Exception(f"发生了未知错误：{e}")
        return "", False
