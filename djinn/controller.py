import re
import json
import argparse
import subprocess
from typing import List
from .cmd import CMD
from .db import Database
from .model import Model
from .log import log, Style
from settings import *


class State:
    """
    State of the controller.
    """
    RUNNING = 0     # already running
    START   = 1     # initially starting
    STOP    = 2     # initially stopping


class Action:
    """
    Action parsed from llm output.
    """
    action: str
    description: str


class Controller:
    """
    Controls program logic and handles all processes.
    """
    def __init__(self):
        self.db = Database(DB_PATH)
        self.model = Model()
        self.cmd = CMD()


    """
    Main execution loop for this controller.
    """
    def run(self) -> None:
        state = State.START

        while not self.stopped:
            if state == State.START:
                # buildup
                state = State.RUNNING

            elif state == State.RUNNING:
                # 1. begin with prompt
                prompt = 'write a program that implements a function in python that multiplies two numbers'

                # query model with (formatted) prompt
                log(Style.cyan, Style.bold, '[prompt]', Style.end, ' ', prompt, '\n')

                result = self.model.query(prompt)

                # iterate over and execute actions, feed output back into model
                self.cmd.execute_instructions(result)

                # 4. evaluate effectiveness of actions AFTER ALL ACTIONS COMPLETED
                # 5. repeat 2-4 until effectiveness sufficient
                # 6. repeat 1-5 until process terminated 

                state = State.STOP

            elif state == State.STOP:       # on initial stop
                # teardown
                self._quit()
                self.stopped = True

            else:
                pass


    """
    Terminates all processes.
    """
    def _quit(self) -> None:
        self.model.quit()
        self.stopped = True
