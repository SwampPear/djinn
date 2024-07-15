from .terminal import Terminal



class STATE:
    """
    App state.
    """
    IDLE = 0
    RUNNING = 1
    STOP = 2


class App:
    """
    Interactive djinn app.

    Params:
        project - the working project
    """
    def __init__(self, project: str):
        self.project = project


    """
    Runns the Djinn app.
    """
    def run(self):
        state = STATE.IDLE
        term = Terminal(self.project)

        while state != STATE.STOP:
            if state == STATE.IDLE:
                prompt = term.poll()
                state = STATE.RUNNING
            elif state == STATE.RUNNING:
                print('running here')
                state = STATE.STOP