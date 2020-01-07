# First Session
In this session, we will build a docker container which runs a simple application that print current date.

## Step To Build
- Copy every file to the server
- Image description is contained in the [Dockerfile](Dockerfile). We will use this file to build the container.
- Run this command to build the image
```
docker build -t <image_tag_name> -f Dockerfile .
```
- See `docker images`, if your docker image has been built successfully, its name will appear on the list.
- To run the image, run
```
docker run -ti <image_tag_name>
```
- If you want to run custom command (for example `bash`), you can use
```
docker run -ti <image_tag_name> bash
```