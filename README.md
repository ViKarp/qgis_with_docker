# qgis_with_docker

This project contains Docker containers to run fastapi server with qgis processing based on a minimal Python script from the command line.

## Example with local image

You can build the base images as described below in the section "Build the container" and then build the example container locally.

In the directory, run the following commands to build the image including the example data, run the container to execute the analysis, and then extract the output files to a local directory relative to the current path.

```bash
xhost +
docker build -t myimage .
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/victor21/fastapi/output:/home/output -v /home/victor21/fastapi/input:/home/input -e DISPLAY=$DISPLAY --rm --name mycontainer -p 80:80 myimage
```
![Alt text](/1.jpg?raw=true "Optional Title")
