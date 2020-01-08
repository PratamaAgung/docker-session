# Fifth Session
**This session required the docker image from the 4th session, please finish the session first**
This session will cover:
- Reuse built image for multiple application
- See the power of port mapping when building multiple similar application

## Step To Build
- Copy every file to the server (please follow the directory structure as in this repo)
- System description is contained in the [`docker-compose.yml`](docker-compose.yml). Please take a look before running the following step.
- Building each image in the system is so simple, just type the command
```
docker-compose build
```
- To run the system in detached mode, use this command
```
docker-compose up -d
```
The command will fire up each service described in `docker-compose.yml`.
