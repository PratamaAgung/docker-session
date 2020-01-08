# docker-session
This repository is intended for sharing session about docker

## Recommended tools
We can play with docker tools using its online labs. It can avoid the time and cumbersome of installing docker on your local machine. This is the steps required to access the labs:
1. Create your Docker Hub user at https://hub.docker.com/, 
2. You can access the labs at https://labs.play-with-docker.com/. Use your Docker Hub user to login

## List of useful command
- `docker images`: List all the images available in the local repository
- `docker ps`: List all running containers
- `docker ps -a`: List all containers (including one that has been exited/created)
- `docker build -t <image_tag_name> -f <Dockerfile path> <build_context>`: build image
- `docker run -ti <image_tag_name>`: run image
- `docker exec -ti <container_id> <command>` : jump into running container and execute command
- `docker kill <container_id>`: stop running container
- `docker rm <container_id>` : delete container
- `docker rmi <image_id>` : delete image
- `docker save <image_tag_name> -o <file>` : export docker image into local file
- `docker load -i <file>` : load docker image from file
- `docker logs <container_id>` : get log of the container. Useful for debugging and monitoring

## Session
- [First Session](session-1) : Build simple appilcation that print current date
- [Second Session](session-2) : Build simple Flask API
- [Third Session](session-3) : Intro to docker-compose
- [Fourth Session](session-4) : Train machine learning model and serve it as an API
- [Fifth Session](session-5) : Reuse docker image built in the 4th session to build greater API system