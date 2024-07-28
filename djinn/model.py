import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from .utils import *


load_dotenv()


class Model:
    def __init__(self, workspace) -> None:
        self.workspace = workspace
        self.client = OpenAI()

    
    def format_context(self) -> str:
        context = read_file(f'{DJINN_DIR}/prompts/basic_context.md')
        context = context.replace('<root_dir>', self.workspace)

        return context


    def query(self, query: str):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.format_context()},
                {"role": "user", "content": query}
            ])
        
        return completion.choices[0].message.content