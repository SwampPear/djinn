import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from .utils import *


load_dotenv()


class Model:
    def __init__(self) -> None:
        self.client = OpenAI()

    def query(self, query: str):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": read_file(f'{DJINN_DIR}/prompts/basic_context.md')},
                {"role": "user", "content": query}
            ])
        
        return completion.choices[0].message.content