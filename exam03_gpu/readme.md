## nvida 플러그인 설치

```
# gpg 키 등록
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)    && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -    && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# 도커 플러그인 설치 
sudo apt-get update
sudo apt-get install -y nvidia-docker2

#서비스 재시작 
sudo systemctl restart docker

# 실행 (ubuntu 이미지 사용함)
docker run --rm --gpus all ubuntu nvidia-smi

```
