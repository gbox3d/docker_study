## docker file 만들기 
```
touch Dockerfile
```

## 이미지 빌드하기
```
docker build . -t study/node-web-app
```

## 생성된 이미지 목록 확인
```
docker images
```

## 이미지를 가지고 컨테이너 등록 (실행)
```
docker run -p 8081:8080 -d study/node-web-app
```

## 실행중인 컨테이너 목록 확인
```
docker ps
```

## 컨테이너 중지
```
```

