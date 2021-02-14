#!/bin/bash
app="oweek-beep-boop"
docker build -t ${app} .
docker run -d -p 1193:80 --name=${app} -v $PWD:/app ${app}
