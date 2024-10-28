# project_billee_2025
Developing for URC 2025

## Docker Commands

`sudo docker image build -t billee .`
`sudo docker run -it --user ros --network=host --ipc=host -v $PWD/:/project_billee_2025 -v /tmp/.X11-unix:/tmp/.X11-unix:rw --env=DISPLAY  billee` - running the command and mounting the project directory as volume
