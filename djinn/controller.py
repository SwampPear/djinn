import subprocess
from .db import Database
from .model import Model
from settings import *
from .utils import prompt



class State:
    RUNNING = 0
    STOPPED = 1
    START   = 2
    STOP    = 3
    TERM    = 4


class Controller:
    """
    Controlls all processes.
    """
    def __init__(self) -> None:
        # modules
        self.db = Database(DB_PATH)
        self.model = Model()

        # state

    """
    Runs the controller.
    """
    def run(self) -> None:
        stop = False
        state = State.START

        while not stop:
            if state == State.START:        # initially starting
                # nothing here now should be intitial tasks to do
                state = State.RUNNING
            elif state == State.RUNNING:    # active state
                # meat and butter

                # 1. begin with prompt
                prompt = 'write a program that implements a function in python that multiplies two numbers'
        
                # 2. format prompt for generation (include context, operational requirements) TODO: prompt generator module
                prompt = prompt(prompt)

                # a. load into model and get output and action sequence (should provide information on how to format correctly)
                result = self.model.query()

                print(result)
                
                # these should also be local to the controller:

                # 3. iterate over and execute actions, feed output back into model
                # 4. evaluate effectiveness of actions AFTER ALL ACTIONS COMPLETED
                # 5. repeat 2-4 until effectiveness sufficient
                # 6. repeat 1-5 until process terminated 

                pass
            elif state == State.STOPPED:    # already stopped
                pass
            elif state == State.STOP:       # on initial stop
                state = State.STOPPED
            elif state == State.TERM:       # program terminated
                self._quit()
            else:
                pass

    """
    Initializes an automated development session.
    """
    def _init(self) -> None:
        # feed prompt into llm
        # take ouput and feed into aterm (automated terminal)
        output = 'ls'
        self._cmd(output)

        # take output from aterm feed into llm
        # repeat
        pass

    """
    Parses and executes a given command.

    Params:
        cmd - the command to parse

    Returns:
        output of the executed command
    """
    def _cmd(self, cmd: str) -> str:
        # Execute the command
        process = subprocess.Popen(
            cmd, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )

        # Get the output and error (if any)
        out, err = process.communicate()

        # Decode bytes to string (assuming utf-8 encoding)
        output_str = out.decode('utf-8')
        error_str = err.decode('utf-8')

        # Print the output and error
        print("Output:", output_str)
        print("Error:", error_str)


    """
    Terminates all processes.
    """
    def _quit(self) -> None:
        self.model.quit()