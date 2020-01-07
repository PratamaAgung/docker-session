# Third Session
This session will cover the introduction to the `docker-compose`. Basically, `docker-compose` will make our life easier by using `yaml`-based file to build and run image. It will be very useful if we have multiple docker container in our system. 

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
