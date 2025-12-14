# Setting up Node.js Development Environment with Docker

```bash

docker run -it -v  ./exam01_node:/works -p 8080:8080 --name hello-nodejs ubuntu:25.10     

```

## Setting up Node.js Environment

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
export NVM_DIR="$HOME/.nvm"
. "$NVM_DIR/nvm.sh"
nvm install --lts
node -v
npm -v
```


## Installing Project Dependencies

```bash
docker exec hello-nodejs bash -lc '
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
node -v
node /works/server.js
'

```
