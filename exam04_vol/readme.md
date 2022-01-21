# 바인드 마운트 예제  

--rm 명령은 실행종료후 컨테이너 자동삭제  
-v 호스트머신용실제디랙토리경로:컨테이너측디랙토리경로  

```sh
# 이미지 이름 study/node_16:step1 실행확인 
docker run -it --rm study/node_16:step1 pwd

# 현제 위치로 볼륨을 마운트 하여 디랙토리 리스팅 수행 
docker run -v `pwd`:/usr/work  -it --rm study/node_16:step1 ls

# node 실행 
docker run -v `pwd`:/usr/work  -it --rm study/node_16:step1 node test.js


docker run -v `pwd`/../:/usr/work  -it --rm study/node_16:step1 ls

#종속모듈설치
docker run -v `pwd`/../exam01_node:/usr/work  -it --rm study/node_16:step1 npm install
#서버 실행
docker run -v `pwd`/../exam01_node:/usr/work  -it --rm -p 24080:8080  study/node_16:step1 npm start

#백그라운드로 실행하기 
docker run -v `pwd`/../exam01_node:/usr/work  -d --rm -p 24080:8080  study/node_16:step1 npm start

```