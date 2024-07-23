import requests
import subprocess
import threading
import json
from .utils import *
from .terminal import log, text, STYLE


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

        log(text('Initializing model...\n', [STYLE.GREEN, STYLE.BOLD]))
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

        log(text('Querying...\n', [STYLE.GREEN, STYLE.BOLD]))
        response = requests.post(url, headers=headers, json=data)

        return(response.json()['message']['content'])

