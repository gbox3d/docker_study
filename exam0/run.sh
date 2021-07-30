#!/bin/bash
# 도커를 실행시켜 php 프로세스를 그안에서 동작시킨다.
docker run --name step2 -p 8000:8000 -it docker_php:step2