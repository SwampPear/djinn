import json


def config(key):
    with open('config.json', 'r') as file:
        return json.load(file)[key]