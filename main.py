from djinn import FileTree
from settings import ROOT


if __name__ == '__main__':
    a = FileTree(ROOT)
    print(a.tree())
