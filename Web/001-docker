# Basics

Running hello world example:

$docker run hello-world

Docker container will be stopped after command execution. To make it working run it as a deamon:
$docker run -d hello-world

For better managing multiple containers it is useful to name the container:
$docker run -d --name my-container hello-world

We can run it in interactive mode using -i (usaually with tty flag -t)
$docker run -it -d --name my-container hello-world

For testing or running container to only do job and stop it is useful to call it with -rm flag, which means that all files (not image) will be removed
$docker run -it -d --name my_container -rm hello-worl

To show running containers
$docker ps

To show all containers
$docker ps -a

To stop container
$docker stop my-container

To show all images
$docker images

To remove image (containers which are using it have to be stopped)a
$docker rmi image-name
or
$docker image remove image-name

# Cleaning

To clean everything:
$docker system prune -a -f

# Dockerfile and docker-compose

Dockerfile is used to build one image. docker-compose is used to runn it (also multicontainer).

Example dockerfile to build nginx server:
```

```

Example docker-compose.yaml file:
```

```

Run docker-compose file using
$docker compose up

It is useful to rebuild the image when reloading after changes in Dockerfile
$docker compose up --build

Can be run in detach mode
$docker compose up --detach --build

Cleanup it
$docker compose down

There can be more than one docker-compose files, it can be run with -f flag:
$docker compose -f name-of-docker-compose-file up --build
It can be used to have development docker enviorment and production
