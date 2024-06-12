class FileBuffer:
    """
    File object to be used by the controller.
    """
    def __init__(self, raw: str):
        self.tab_size = 4
        self.raw = raw
        