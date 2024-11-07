FROM osrf/ros:humble-desktop

# update and clear package lists
RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/* 

ARG ROS_DISTRO="humble"
ARG USER="root"


# MUST INCLUDE -y in order to auto accept y/n when using apt-get to install gazebo, otherwise will abort
RUN sudo apt-get update \ 
    && apt-get install ros-${ROS_DISTRO}-xacro \
    && rm -rf /var/lib/apt/lists/*

RUN sudo apt-get update \ 
    && apt-get -y install ros-${ROS_DISTRO}-gazebo-ros-pkgs \ 
    && rm -rf /var/lib/apt/lists/*

RUN sudo apt-get update \ 
    && sudo apt-get -y install jstest-gtk \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
#COPY bashrc /home/${USERNAME}/.bashrc

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["bash"]

