
## 그냥하는 방법
### build
```
docker pull mongo:4
```

### run

-v 마운트될위치지정(서로 연결시킬 폴더지정)
```
docker run --name mongodb-container -v ~/data:/data/db -d -p 27017:27017 mongo
```

## docker-compose.yml 파일로 하는 방법

### docker-compose install

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

```



### build
```
docker-compose build
```

### run
```
docker-compose up -d
``` 
