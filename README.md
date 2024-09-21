# Install
Clone repository and change directory
```
git clone https://github.com/fedoxyz/RealTimeCV
cd RealTimeCV
```

Build from Dockerfiles
```
cd server && docker build -t server .
cd ../client && docker build -t client .
```

Be sure to have nvidia-container-toolkit installed on your host machine to run with GPU.

Run containers for server and client images
```
docker run --rm --gpus all -p 5000:5000 server
docker run -p 80:80 client
```
