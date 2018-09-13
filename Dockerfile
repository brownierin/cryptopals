FROM python:2.7-slim

COPY requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /cryptopals/set_01
COPY . /cryptopals
