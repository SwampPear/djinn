from .terminal import Terminal, STYLE



class STATE:
    IDLE = 0
    RUNNING = 1
    STOP = 2


class App:
    """
    Interactive djinn app.
    """
    def __init__(self, project: str):
        self.project = project


    def run(self):
        state = STATE.IDLE
        term = Terminal(self.project)

        while state != STATE.STOP:
            if state == STATE.IDLE:
                term.poll()
                state = STATE.RUNNING
            elif state == STATE.RUNNING:
                print('running here')
                state = STATE.STOP