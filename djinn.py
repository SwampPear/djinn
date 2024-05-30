import sys
from djinn import Controller


if __name__ == '__main__':
    prompt = sys.argv[1]

    controller = Controller(prompt)

    controller.run()
