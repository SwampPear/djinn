import json
import logging
from datetime import datetime


def read_json(fp):
    with open(fp, 'r') as file:
        return json.load(file)


def logp(level, message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"[{time}] \033[92m[{level}]\033[0m {message}")


def logi(level, message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"[{time}] \033[96m[{level}]\033[0m {message}")


def logn(level, message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.error(f"[{time}] [\033[91m[{level}]\033[0m] {message}")