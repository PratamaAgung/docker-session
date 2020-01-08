# Fourth Session
This session will cover:
- Training and serving machine learning model (ARIMA) as an API
- Orchestrate services using `docker-compose`. We will have two services: `ml-model` will build and train the model, `flask-app` will serve the API and use the result of `ml-model` for prediction.
- Use volume mounting to share file between containers.

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
