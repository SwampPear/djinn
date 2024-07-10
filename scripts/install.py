import subprocess
import json

base_user_settings = {
    "test_setting": "this is a test settings"
}


def main():
    # init lib dir
    subprocess.call(['sudo', 'rm',  '-rf', '/Library/Djinn'])
    subprocess.call(['sudo', 'mkdir',  '/Library/Djinn'])
    subprocess.call(['sudo', 'chmod',  '777', '/Library/Djinn'])

    # copy start script
    subprocess.call(['sudo', 'cp', './djinn.py', '/Library/Djinn/'])

    # init data dir
    subprocess.call(['sudo', 'rm',  '-rf', '/var/db/Djinn'])
    subprocess.call(['sudo', 'mkdir',  '/var/db/Djinn'])
    subprocess.call(['sudo', 'chmod',  '777', '/var/db/Djinn'])

    # init user data dir
    subprocess.call(['sudo', 'rm',  '-rf', '/var/db/Djinn/user'])
    subprocess.call(['sudo', 'mkdir',  '/var/db/Djinn/user'])

    # TODO: fix permissions with this
    # init user settings
    with open('/var/db/Djinn/user/settings.json', 'w') as out:
        subprocess.call(['sudo', 'echo', json.dumps(base_user_settings)], stdout=out)

    # init projects data dir
    subprocess.call(['sudo', 'rm',  '-rf', '/var/db/Djinn/projects'])
    subprocess.call(['sudo', 'mkdir',  '/var/db/Djinn/projects'])

    # copy lib to lib dir
    subprocess.call(['sudo', 'cp', '-r', './djinn', '/Library/Djinn/djinn'])

    # TODO: install pip requirements when necessary (requirements.txt)

if __name__ == '__main__':
    main()
