import subprocess
import os
import json

base_user_settings = {
    "test_setting": "this is a test settings"
}


def main():
    lib_dir = f'{os.path.expanduser("~")}/Library/Application\ Support/Djinn'

    # init lib dir
    subprocess.call(['rm',  '-rf', lib_dir])
    subprocess.call(['mkdir',  lib_dir])

    # copy start script
    subprocess.call(['cp', './djinn.py', lib_dir])

    # init user data dir
    subprocess.call(['rm',  '-rf', f'{lib_dir}/user'])
    subprocess.call(['mkdir',  f'{lib_dir}/user'])

    # init user settings
    subprocess.call(['touch', f'{lib_dir}user/settings.json'])
    with open(f'{lib_dir}/user/settings.json', 'w') as file:
        json.dump(base_user_settings, file)

    # init projects data dir
    subprocess.call(['sudo', 'rm',  '-rf', f'{lib_dir}/projects'])
    subprocess.call(['sudo', 'mkdir',  f'{lib_dir}/projects'])

    # copy lib to lib dir
    subprocess.call(['sudo', 'cp', '-r', './djinn', f'{lib_dir}/djinn'])

    # TODO: install pip requirements when necessary (requirements.txt)

if __name__ == '__main__':
    main()
