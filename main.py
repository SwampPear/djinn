import os
import sys
from djinn.djinn import Djinn

"""
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv
"""

def main():
    try:
        # parse
        args = sys.argv[1:]
        fp = args[0]

        dj = Djinn(fp)
        dj()

    except IndexError:
        print("No arguments provided.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()