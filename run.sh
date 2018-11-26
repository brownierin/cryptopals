#!/bin/bash

docker build -t cryptopals . 
docker run --name cryptopals -it cryptopals bash
