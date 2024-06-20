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
    def __init__(self, 
        path: str,
        is_dir: bool = False, 
        contents: str = '', 
        children: List[Self]=[]):

        self.path = path
        self.is_dir = is_dir
        self.contents = contents
        self.children = children


class FileTree:
    """
    Represents a system of files and directories.

    Params:
        path - path of file or directory
    """
    def __init__(self, path):
        self.head = self._init_head(path)
        #print(self.tree(self.head))

    
    """
    Called when casting a FileTree to a string.
    """
    def s(self, node=None) -> str:
        if not node:
            self.s(node=self.head)
        else:
            print(node.path)

            for child in node.children:
                self.s(node=child)

    """
    Formats a string defining the structure of this file tree.
    """
    def tree(self, node, level=0) -> str:
        output = ''
        name = node.path.split('/')[-1]

        # indentation level
        if level == 0:
            output += '. '
        else:
            output += (level - 1) * ' '
            output += '|_ '

        # file/dir name
        output += f'{name}\n'
        print(output)

        for ch in node.children:
            output += self.tree(ch, level = level + 1)

        return output


    """
    Initializes the head node of this file tree.

    Params:
        path - the path of the head node
    """
    def _init_head(self, path: str) -> FileNode:
        node = FileNode(path)

        if os.path.isdir(path):
            for el in os.listdir(path):
                fmt_path = f'{path}/{el}'
                is_dir = os.path.isdir(fmt_path)
                new_node = self._init_head(fmt_path)

                if is_dir:
                    # recurse
                    new_node.is_dir = True

                    print(fmt_path)
                else:
                    new_node.contents = 'file'
                    print(fmt_path)

                node.children.append(new_node)

            return node
        else:
            return node

        