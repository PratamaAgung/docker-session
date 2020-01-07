# docker-session
This repository is intended for sharing session about docker

## List of useful command
- `docker images`: List all the images available in the local repository
- `docker ps`: List all running containers
- `docker ps -a`: List all containers (including one that has been exited/created)
- `docker build -t <image_tag> -f <Dockerfile path> <build_context>`: build image
- `docker run -ti <image_tag>`: run image
- `docker exec -ti <container_id> <command>` : jump into running container and execute command
- `docker stop <container_id>`: stop running container
- `docker rm <container_id>` : delete container
- `docker rmi <image_id>` : delete image

## Session
- [First Session](session-1) : Build simple appilcation that print current date