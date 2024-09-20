```
git clone https://github.com/fedoxyz/RealTimeCV
cd RealTimeCV
cd server && docker build -t server . &
cd client && docker build -t client . &
docker run -p 5000:5000 server
docker run -p 80:80 client
```
