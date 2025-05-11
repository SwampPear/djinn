import sys
from djinn.utils import read_json


def main():
    try:
        args = sys.argv[1:]
        config = read_json(args[0])


        print(config)
    except IndexError:
        print("No arguments provided.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()