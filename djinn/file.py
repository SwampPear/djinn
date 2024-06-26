import os
from typing import List, Self


class FileBuffer:
    """
    File object to be used by the controller.
    """
    def __init__(self, raw: str):
        self.tab_size = 4
        self.raw = raw


class FileNode:
    """
    Represents a single file or directory

    Params:
        name - name of the file or directory
        is_dir - true if object is dir, false otherwise
        contents - contents of a file
        children - children of a directory
    """
    def __init__(self, path: str):
        self.path = path
        self.is_dir = True
        self.contents = ''
        self.children = []

    """
    String representation of FileNode.
    """
    def __str__(self) -> str:
        if self.is_dir:
            return f'path: {self.path}, ch: {len(self.children)}'
        else:
            return f'path: {self.path}, contents: {self.contents}'

    """
    Returns the name of this node.
    """
    def name(self) -> str:
        return self.path.split('/')[-1]


class FileTree:
    """
    Represents a system of files and directories.

    Params:
        path - path of file or directory
    """
    def __init__(self, path: str):
        self.path = path
        self.head = FileNode(self.path)
        self.parse(self.head)


    """
    Parses the directory tree of a given node
    """
    def parse(self, node: FileNode) -> None:
        path = node.path

        if os.path.isdir(path):                         # directory
            for ls in os.listdir(path):
                # create new node
                fmt_path = f'{path}/{ls}'
                print(fmt_path)
                new_node = FileNode(fmt_path)

                # add new node to children
                node.children.append(new_node)

                # parse from new node
                self.parse(new_node)
        else:                                           # file
            node.is_dir = False
            node.contents = 'read contents'
