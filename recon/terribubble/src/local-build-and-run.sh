#!/bin/bash
app="oweek-terribubble"
docker build -t ${app} .
docker run -d -p 1093:80 --name=${app} -v $PWD:/app ${app}
