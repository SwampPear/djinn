import os
from openai import OpenAI
from dotenv import load_dotenv
from djinn.prompts import enumerate_tasks_prompt
from djinn.utils import read_json


load_dotenv()


class Djinn:
    def __init__(self, config_fp):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        self.config = read_json(config_fp)


    def __call__(self) -> None:
        # lists all tasks for project completion
        self._enumerate_tasks()


        print('adsf')


    def _query(self, prompt):
        res = self.client.chat.completions.create(model='gpt-4',
        messages=[
            {"role": "user", "content": prompt}
        ])

        print(res.choices[0].message.content)


    def _enumerate_tasks(self):
        prompt = enumerate_tasks_prompt(self.config)

        self._query(prompt)