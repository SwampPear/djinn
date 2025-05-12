import os
import json
import subprocess
from openai import OpenAI
from dotenv import load_dotenv
from djinn.utils import read_json, logp, logn, logi
import djinn.prompts as p

load_dotenv()

DEFAULT_CONFIG_FP = "config.json"

class Djinn:
    """
    Handles task planning and execution.
    """


    def __init__(self):
        """
        Initializes the Djinn instance.
        """
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.config = read_json(DEFAULT_CONFIG_FP)

        logp("djinn", "initialized")


    def run(self) -> None:
        """
        Executes project implementation workflow by enumerating tasks and
        executing these tasks.
        """
        logp("djinn", "started")

        tasks = self._enumerate_tasks()

        logp("djinn", "tasks generated")
        
        self._execute_tasks(tasks)


    def _query(self, prompt):
        """
        Sends a prompt to the OpenAI API and retrieves the response.

        Args:
            prompt (str): The prompt to send to the OpenAI API.

        Returns:
            str: The content of the response message from the API.
        """
        res = self.client.chat.completions.create(model='gpt-4',
        messages=[
            {"role": "user", "content": prompt}
        ])

        return res.choices[0].message.content

    def _enumerate_tasks(self):
        """
        Generates a list of tasks.

        Returns:
            list: A list of tasks represented as JSON objects.
        """
        res = self._query(p.enumerate_tasks(self.config))
        tasks = json.loads(res)

        return tasks
    
    def _execute_tasks(self, tasks):
        """
        Executes a list of tasks by running their associated shell commands.

        Args:
            tasks (list): A list of task dictionaries, each containing a description and an action.
        """
        for _task in tasks:
            _action = _task["action"] if len(_task["action"]) < 64 else _task["action"][:61] + "..."

            if _task["type"] == "input":
                logi(_task["type"], f"({_task["file"]}) {_action}")

                self._cmd(_task['action'])
            elif _task["type"] == "output":
                logp(_task["type"], _action)

                self._cmd(_task['action'])

    def _cmd(self, command):
        """
        Executes a shell command and returns its output. Logs any errors encountered during execution.

        Args:
            command (str): The shell command to execute.

        Returns:
            str: The standard output of the command, or an error message if execution fails.
        """
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            return result.stdout
        
        except subprocess.CalledProcessError as e:
            logn("error", e)

            return f"An error occurred while executing the command: {e}"