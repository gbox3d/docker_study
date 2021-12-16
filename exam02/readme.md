## 우분투 실행시키기  

```sh
docker pull ubuntu:lastest
docker create -it --name ubuntu-1 ubuntu
docker start ubuntu-1

docker exec -it ubuntu-1 /bin/bash # bash 실행

docker exec -it ubuntu-1 python3 -V # python3 version check 


```

