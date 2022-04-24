docker build -t web:v1 . && docker run -d --rm -p 9090:80 --name flusk web:v1
docker logs flusk