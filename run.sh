#!/bin/bash

docker build -t cryptopals . 
docker run -it --rm cryptopals bash
