#!/bin/bash

# init lib dir
sudo mkdir /Library/Djinn

# init startup script
sudo cp djinn.py /Library/Djinn/djinn.py

# init data
sudo mkdir /var/db/Djinn
sudo rm /var/db/Djinn/data
sudo touch /var/db/Djinn/data

# copy lib contents
sudo rm -rf /Library/Djinn/djinn
sudo cp -r djinn/ /Library/Djinn/djinn