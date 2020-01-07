# Second Session
In this session, we will build a simple Flask API. We will use port mapping to expose certain port to the outside world.

## Step To Build
- Copy every file to the server
- Image description is contained in the [Dockerfile](Dockerfile). From the Dockerfile, we can see that the application will expose its 5000 port for serving the incoming request.
- Run this command to build the image
```
docker build -t <image_tag_name> -f Dockerfile .
```
- See `docker images`, if your docker image has been built successfully, its name will appear on the list.
- To run the image, run the following 
```
docker run -ti -p "<local_port>:<docker_port>" <image_tag_name>
```