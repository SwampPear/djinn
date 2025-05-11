def enumerate_tasks_prompt(config):
    root        = config['root']
    role        = config['role']
    project     = config['project']
    stack       = config['stack']
    environment = config['stack']
    format = '''
    {
        'tasks': [
            {
                'description': <task description>
                'action': <terminal command>,
            }
        ],
    }
    '''

    prompt = f'''
    Your role is a {role}. Please enumerate the tasks required to implement the following project based on the description provided. 
    The tasks should be detailed and ordered in a logical sequence, considering dependencies and priorities. 
    The project description is as follows: 
    "{project}"

    The root directory for all paths used in this project should be: {root}

    The reccomended stack: {stack}

    The computer environment: {environment}

    The output format from this prompt should AT ALL TIMES be json serializable and follow the following format:

    {format}

    The action SHOULD ONLY be a command that can be run in the terminal without error.
    '''

    return prompt