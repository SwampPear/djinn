import os
import sys


sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


import unittest
from tests.testDatabase import TestDatabase


if __name__ == '__main__':
    unittest.main()