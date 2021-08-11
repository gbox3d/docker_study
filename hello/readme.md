## build image

```
docker build . -t hello-node:step1
```

## create continer

```
docker create -it --name test-ct hello-node:step1
```


## run
```
docker run -itd --name test-ct hello-node:step1
```

## exec
실행중인 컨테이너에서 특정 명령어 실행  
-w 작업디랙토리
```
docker exec -it -w /home f3be1b3d223e ls 
```
