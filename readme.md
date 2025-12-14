## 기본 명령어

```sh

docker images # 도커 이미지 목록

docker ps # 컨테이너 목록
docker ps -a # 컨테이너 목록( 실행중단된 컨테이너 포함)

```

## 컨터이너 만들기

```sh
docker run -it --name 컨테이너이름 이미지이름:태그 /bin/bash
docker run -it --name hello-docker ubuntu:25.10 bash


docker start 컨테이너이름 # 컨테이너 시작
docker stop 컨테이너이름  # 컨테이너 중지

docker start hello-docker
docker exec -it hello-docker bash # 실행중인 컨테이너에 접속


docker commit 컨테이너이름 이미지이름:태그 # 컨테이너를 이미지로 저장
docker commit hello-docker uv-offline:1.0 # 컨테이너를 이미지로 저장

docker rm 컨테이너이름 # 컨테이너 삭제
docker rm hello-docker

docker run --rm 이미지이름:태그 /경로/실행파일 # 컨테이너 실행 후 종료 및 삭제
docker run --rm uv-offline:1.0 /works/.venv/bin/python /works/main.py # 이미지로 컨테이너 실행 후 종료

docker run --rm -v 호스트경로:컨테이너경로 이미지이름:태그 /경로/실행파일 # 볼륨 마운트하여 컨테이너 실행

docker save -o 파일이름.tar 이미지이름:태그 # 이미지를 tar 파일로 저장
docker save -o uv-offline_1.0.tar uv-offline:1.0 # 이미지를 tar 파일로 저장

docker load -i 파일이름.tar # tar 파일로 이미지 불러오기
docker load -i uv-offline_1.0.tar # tar 파일로 이미지 불러오기

```

## uv 환경 만들기
```sh

apt update
apt install curl ca-certificates vim iproute2
curl -LsSf https://astral.sh/uv/install.sh | sh

echo 'source $HOME/.local/bin/env' >> ~/.bashrc
source ~/.bashrc

``` 

