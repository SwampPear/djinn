import requests
import subprocess
import threading


class Model:
    """
    Provides an interface for interacting with a locally hosted llama3 instance.
    """
    def __init__(self) -> None:
        # init llama process
        self.llama3_thread_pid = -1
        self.llama3_thread = threading.Thread(target=self._init_llama_thread)
        self.llama3_thread.start()

        self._sync_llama3_thread_pid()

        self.quit()

        # wait for thread to finish
        self.llama3_thread.join()


    """
    Queries the llama server.
    """
    def query(self, prompt) -> None:
        url = 'http://localhost:11434/api/chat'

        data = {
            'model': 'llama3',
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
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
    Terminates the llama server.
    """
    def quit(self) -> None:
        process = subprocess.Popen(
            ['kill', '-9', str(self.llama3_thread_pid)], 
            shell=True,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )

        process.communicate()

    """
    Initializes the llama server thread.
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
        while self.llama3_thread_pid == -1:
            pass