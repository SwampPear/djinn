from .terminal import Terminal
from .cmd import CMD
from .db import Database
from .model import Model
from .utils import DJINN_DIR



class STATE:
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
    """
    def __init__(self, project: str):
        self.project = project
        self.db = Database(f'{DJINN_DIR}/projects/{project}/data')
        self.model = Model()
        self.cmd = CMD()


    """
    Runns the Djinn app.
    """
    def run(self) -> None:
        state = STATE.IDLE
        term = Terminal(self.project)
        prompt = ''

        while state != STATE.STOP:
            if state == STATE.IDLE:
                prompt = term.prompt()

                """
                if prompt:
                    state = STATE.RUNNING
                else:
                    state = STATE.IDLE
                """
                state = STATE.RUNNING
              
            elif state == STATE.RUNNING:
                # query model for actions and execute
                # result = self.model.query(prompt)
                #self.cmd.execute_instructions(result)

                # 1. begin with prompt
                # 2. query model with (formatted) prompt
                # 3. iterate over and execute actions, feed output back into model
                # 4. evaluate effectiveness of actions AFTER ALL ACTIONS COMPLETED
                # 5. repeat 2-4 until effectiveness sufficient
                # 6. repeat 1-5 until process terminated 
                
                state = STATE.STOP

        self._quit


    """
    Terminates all processes.
    """
    def _quit(self) -> None:
        self.model.quit()
        #self.stopped = True