import json


def read_json(fp):
    with open(fp, 'r') as file:
        return json.load(file)