FROM ubuntu:20.04
WORKDIR /usr/work/

RUN apt-get update
RUN apt-get install -y vim net-tools openssh-server curl wget
#node js 설치 
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
RUN apt-get install -y nodejs
    
