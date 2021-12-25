## 우분투 실행시키기  

```sh
docker pull ubuntu:lastest
docker create -it --name ubuntu-1 ubuntu
docker start ubuntu-1

docker exec -it ubuntu-1 /bin/bash # bash 실행

파이썬 설치 
apt install python3
apt install python3-pip

docker exec -it ubuntu-1 python3 -V # python3 version check 

docker exec -it ubuntu-1 mkdir /work # 새로운 디렉토리 생성

docker cp test.py ubuntu-1:/work # test.py 컨테이너로 복사 

docker exec -it -w /app ubuntu-1 python3 test.py # test.py 실행

```
# import export

```sh
docker export -o test_con_1.tar ubuntu-1
docker import --change 'CMD ["/bin/bash"]' test_con_1.tar ubuntu_test # 이미지 복원

docker run -it --rm -w /work ubuntu_test python3 test.py # 컨테이너 실행
```

## 도커 정리하기

```sh
docker rmi $(docker images -a -q) # 전체 이미지 삭제
docker rm -f $(docker ps -a -q) # 전체 컨테이너 삭제
```
