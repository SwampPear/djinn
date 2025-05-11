import sys
from djinn.utils import read_json
from djinn.prompt import enumerate_tasks


def main():
    try:
        args = sys.argv[1:]

        config = read_json(args[0])

        a = enumerate_tasks(config)


        print(a)
    except IndexError:
        print("No arguments provided.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()