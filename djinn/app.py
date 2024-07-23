from .terminal import Terminal
from .cmd import CMD
from .db import Database
from .model import Model
from .utils import DJINN_DIR


class State:
    """
    App state.
    """
    IDLE = 0
    RUNNING = 1
    STOP = 2


class Action:
    """
    Action parsed from llm output.
    """
    action: str
    description: str


class App:
    """
    Interactive djinn app.

    Params:
        project - the working project
        prompt - a prompt
    """
    def __init__(self, project: str, prompt: str):
        self.project = project
        self.prompt = prompt
        self.db = Database(f'{DJINN_DIR}/projects/{project}/data')
        self.model = Model()
        self.cmd = CMD()
        self.terminal = Terminal(self.project)

        self.state = State.STOP


    """
    Runns the Djinn app.
    """
    def run(self) -> None:
        # query model for instructions
        result = self.model.query(self.prompt)
        
        # execute instructions
        self.cmd.execute_instructions(result)

        self.quit()


    """
    Terminates all processes.
    """
    def quit(self) -> None:
        self.model.quit()