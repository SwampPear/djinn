import subprocess
import os
import json


base_user_settings = {
    "test_setting": "this is a test settings"
}


def main():
    djinn_dir = f'{os.path.expanduser("~")}/Library/Application\ Support/Djinn'
    
    os.rmtree(djinn_dir, ignore_errors=True)    # clear

    os.mkdir(djinn_dir)                 # make djinn dir
    os.mkdir(f'{djinn_dir}/user')       # make user dir
    os.mkdir(f'{djinn_dir/}projects')   # make projects dir

    # copy startup script
    subprocess.call(['cp', './djinn.py', f'{djinn_dir}/djinn.py'])

    # init user settings
    with open(f'{djinn_dir}/user/settings.json', 'w') as file:
        json.dump(base_user_settings, file)

    # copy lib
    subprocess.call(['sudo', 'cp', '-r', './djinn', f'{djinn_dir}djinn'])


if __name__ == '__main__':
    main()
