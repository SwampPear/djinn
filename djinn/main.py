import sys
import logging
from djinn import Djinn
from utils import logn


def main():
    logging.basicConfig(level=logging.INFO)
    
    try:
        dj = Djinn()
        dj.run()

    except Exception as e:
        logn(f"An error occurred: {e}")


if __name__ == '__main__':
    main()