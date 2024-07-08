#!/bin/bash

docker stop djinn-container
docker rm djinn-container
docker run --name djinn-container -d -p 8000:8000 djinn