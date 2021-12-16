## 우분투 실행시키기  

```sh
docker pull ubuntu:lastest
docker create -it --name ubuntu-1 ubuntu
docker start ubuntu-1

docker exec -it ubuntu-1 /bin/bash # bash 실행

docker exec -it ubuntu-1 python3 -V # python3 version check 

docker exec -it ubuntu-1 mkdir /app # 새로운 디렉토리 생성

docker cp test.py ubuntu-1:/app # test.py 컨테이너로 복사 

docker exec -it -w /app ubuntu-1 python3 test.py # test.py 실행

```

