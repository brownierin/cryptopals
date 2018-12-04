FROM python:2.7-slim

RUN apt -y update && apt -y install build-essential

COPY requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /cryptopals/set_02
COPY . /cryptopals
