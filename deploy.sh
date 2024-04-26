docker build -t puska-farm-websocket .
docker run --name puska-farm-websocket -p 8765:8765 --env-file .env --restart always -d puska-farm-websocket:latest