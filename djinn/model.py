import requests
import subprocess
import threading
import json
from .utils import *

# TODO: implement model memory (prompt caching) 
# could possibly be handled through 'messages' field of api call


class PidStatus:
    """
    Process id status.
    """
    NOT_INITIALIZED = -1


class Model:
    """
    Provides an interface for interacting with a locally hosted llama3 instance.
    """
    def __init__(self) -> None:
        self.llama3_thread_pid = PidStatus.NOT_INITIALIZED
        self.llama3_thread = self._init_llama()


    """
    Queries the llama3 server.

    Params:
        prompt - prompt to query the model with

    Returns:
        response from server
    """
    def query(self, prompt: str) -> str:
        url = 'http://localhost:11434/api/chat'

        data = {
            'model': 'llama3',
            'messages': [
                {
                    'role': 'user',
                    'content': self._fmt_prompt(prompt)
                }
            ],
            'stream': False
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, json=data)

        return(response.json()['message']['content'])


    """
    Terminates the llama3 server.
    """
    def quit(self) -> None:
        process = subprocess.Popen(
            ['kill', '-9', str(self.llama3_thread_pid)], 
            shell=True,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )

        process.communicate()

        self.llama3_thread.join()


    """
    Initializes the llama3 server.
    """
    def _init_llama(self) -> None:
        llama3_thread = threading.Thread(target=self._init_llama_thread)
        llama3_thread.start()

        self._sync_llama3_thread_pid()

        return llama3_thread


    """
    Initializes the llama3 server thread.
    """
    def _init_llama_thread(self) -> None:
        process = subprocess.Popen(
            ['ollama run llama3'], 
            shell=True,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )

        self.llama3_thread_pid = process.pid

    
    """
    Syncs the llama server thread pid.
    """
    def _sync_llama3_thread_pid(self) -> None:
        # TODO: add timeout functionality
        while self.llama3_thread_pid == PidStatus.NOT_INITIALIZED:
            pass

    """
    Formats a prompt into and intermediate representation.
    """
    def _fmt_prompt(self, prompt: str):
        fmt_prompt = {}
        fmt_prompt['objective'] = prompt
        fmt_prompt['context'] = read_file('prompts/basic_context.txt')

        print(fmt_prompt)

        return json.dumps(fmt_prompt)
