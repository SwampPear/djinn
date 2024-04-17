import json
 
# Opening JSON file
f = open('data.json')

def config(key):
    with open("config.json") as file:
        data = json.load(file)
        
        return data[key]