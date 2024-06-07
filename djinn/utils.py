import json


"""
Reads content from a file.
"""
def read(path: str) -> str:
    contents = ''

    with open(path, 'r') as file:
        contents = file.read()

    return contents


"""
Formats a prompt into and intermediate representation.
"""
def prompt():
    prompt = {}
    prompt['objective'] = 'do what is said in th'
    prompt['context'] = 'you are an llm with the power to perform simple terminal commands, how should you be implemented'

    print(prompt)

    return json.dumps(prompt)