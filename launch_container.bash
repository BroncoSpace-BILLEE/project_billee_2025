xhost +

sudo docker run -it --network=host --ipc=host \
	-v $PWD/:/project_billee_2025 \
	-v /tmp/.X11-unix:/tmp/.X11-unix:rw --env=DISPLAY \
	--device=/dev/input:/dev/input --device-cgroup-rule='c 13:* rmw' \
	--device=/dev/video0:/dev/video0 --device-cgroup-rule='c 13:* rmw' \
	--device=/dev/video1:/dev/video1 --device-cgroup-rule='c 13:* rmw' \
	--device=/dev/video2:/dev/video2 --device-cgroup-rule='c 13:* rmw' \
	--device=/dev/dri/renderD128:/dev/dri/renderD128 --device-cgroup-rule='c 13:* rmw'\
	billee

