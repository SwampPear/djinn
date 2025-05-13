import logging
from djinn.djinn import Djinn
from djinn.utils import logn


def main():
    logging.basicConfig(level=logging.INFO)
    
    try:
        dj = Djinn()
        dj.run()

    except Exception as e:
        logn(f"An error occurred: {e}")


if __name__ == '__main__':
    main()