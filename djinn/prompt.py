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
Formats a prompt into an xml representation.
"""
def format_prompt():
    prompt = {}
    prompt['objective'] = 'do what is said in the context'
    prompt['context'] = 'you are an llm with the power to perform simple terminal commands, how should you be implemented'

    return json.dumps(prompt)