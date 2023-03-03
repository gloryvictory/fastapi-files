#!/bin/bash
rm -rf /var/zsniigg/fastapi-files/
cp -r /ftp/2/* /var/zsniigg/
sudo chmod -R 777 /var/zsniigg/fastapi-files/
cd /var/zsniigg/fastapi-files/
docker build . -t fastapi-files
# docker run -p 8001:8001 fastapi-files
# docker run -d -p 8001:8001 fastapi-files
# docker rmi fastapi-files
# docker ps
# docker stop <container>
# docker rm <container>
# docker images
# docker rmi <image>


