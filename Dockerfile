# syntax=docker/dockerfile:1

# python distro
FROM python:3.8-slim-buster

# init work dir
WORKDIR /app

# set up python environment
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy contents
COPY . .

RUN mkdir -p /data

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]
