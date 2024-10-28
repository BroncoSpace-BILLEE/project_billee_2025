# Using Docker

## Prerequisites

1. You are on Ubuntu 22.04

## Setting up Docker

The instructions to install Docker can be accessed [here](https://docs.docker.com/engine/install/ubuntu/). We will be using installation method 1 (Install using the `apt` repository). The steps will be detailed below:


### 1. Set up Docker's apt repository:

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### 2.Install Docker Packages

`sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

**Congratulations!** You have now set up docker on your machine.

### Verifiying Installation

You can run the following to make sure that the installation was successful:

`sudo docker run hello-world`

If the installation was successful, you should get the following output in your terminal:

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
```

If you get the following error: `docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`, then simply restart the docker daemon by running `sudo service docker restart` and try again.

## Docker Images

### Important Commands

- `docker image ls` - displays all docker images installed on your machine
- `docker image pull` - downloads the docker image from dockerhub
- `docker image rm ` - removes docker image from your machine
- `docker run` - spawns a container based on a docker image
- `docker container ls` - list containers currently running
- `docker container prune` - removes all stopped containers
- `docker exec` - executes commands inside container

### Inspecting Containers

Using `docker run -it <image_name>`, you can run the container based on the image and execute commands in the container (`it` stands for interactive terminal)

You can exit the container by typing `exit` or hitting `Ctrl + d` while inside the container

You can also stop the container by typing `docker container stop` in the terminal. **This does not delete the container!** If you add the `rm` flag when running the container, it will auto delete the container upon stopping.



