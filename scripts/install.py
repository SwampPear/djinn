import subprocess
import os
import json

base_user_settings = {
    "test_setting": "this is a test settings"
}


def main():
    djinn_dir = f'{os.path.expanduser("~")}/Library/Application\ Support/Djinn'
    
    # init lib dir
    subprocess.call(['rm',  '-rf', djinn_dir])
    subprocess.call(['mkdir',  djinn_dir])

    # copy start script
    subprocess.call(['cp', './djinn.py', djinn_dir])

    # init user data dir
    subprocess.call(['rm',  '-rf', f'{djinn_dir}/user'])
    subprocess.call(['mkdir',  f'{djinn_dir}/user'])

    # init user settings
    subprocess.call(['touch', '~/Library/Application\ Support/Djinn/user/settings.json'])
    with open('~/Library/Application\ Support/Djinn/user/settings.json', 'w') as file:
        json.dump(base_user_settings, file)

    # init projects data dir
    subprocess.call(['sudo', 'rm',  '-rf', '~/Library/Application\ Support/Djinn/projects'])
    subprocess.call(['sudo', 'mkdir',  '~/Library/Application\ Support/Djinn/projects'])

    # copy lib to lib dir
    subprocess.call(['sudo', 'cp', '-r', './djinn', '~/Library/Application\ Support/Djinn/djinn'])

    # TODO: install pip requirements when necessary (requirements.txt)

if __name__ == '__main__':
    main()
