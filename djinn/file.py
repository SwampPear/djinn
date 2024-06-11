class FileBuffer:
    def __init__(self, contents):
        self.lines = contents.split('\n')
        