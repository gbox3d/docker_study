FROM ubuntu:25.10

# 필수 패키지
RUN apt update && apt install -y \
    curl ca-certificates xz-utils \
 && rm -rf /var/lib/apt/lists/*

# Node.js 공식 바이너리 설치 (PATH 자동)
WORKDIR /tmp
RUN curl -LO https://nodejs.org/dist/v20.11.1/node-v20.11.1-linux-x64.tar.xz \
 && tar -xJf node-v20.11.1-linux-x64.tar.xz \
 && cp -r node-v20.11.1-linux-x64/* /usr/local/

# 앱 코드 위치
WORKDIR /works
COPY . /works

# 서버 포트
EXPOSE 8080

# 완전 실행형
ENTRYPOINT ["node", "server.js"]
