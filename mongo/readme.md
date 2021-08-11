## build
```
docker pull mongo:4
```

## run

-v 마운트될위치지정(서로 연결시킬 폴더지정)
```
docker run --name mongodb-container -v ~/data:/data/db -d -p 27017:27017 mongo
```