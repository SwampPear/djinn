#!/bin/bash

# init lib dir
sudo mkdir /Library/Djinn

# init startup script
sudo cp djinn.py /Library/Djinn/djinn.py

# init data dir
sudo mkdir /var/db/Djinn

# init database
sudo rm /var/db/Djinn/data
sudo touch /var/db/Djinn/data

# init projects dir (for project settings)
sudo rm /var/db/Djinn/projects
sudo touch /var/db/Djinn/projects

# init user settings file
sudo rm /var/db/Djinn/settings.json
sudo cp settings.json /var/db/Djinn/settings.json

# copy lib
sudo rm -rf /Library/Djinn/djinn
sudo cp -r djinn/ /Library/Djinn/djinn

# copy env
sudo rm -rf /Library/Djinn/djinn-env
sudo cp -r djinn-env/ /Library/Djinn/djinn-env