xhost +

sudo docker run -it --network=host --ipc=host -v $PWD/:/project_billee_2025 -v /tmp/.X11-unix:/tmp/.X11-unix:rw --env=DISPLAY --device=/dev/input:/dev/input --device-cgroup-rule='c 13:* rmw' billee

