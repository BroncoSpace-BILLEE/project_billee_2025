FROM osrf/ros:humble-desktop

# update and clear package lists
RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/* 

ARG USERNAME=ros
ARG USER_UID=1234
ARG USER_GID=$USER_UID
ARG ROS_DISTRO="humble"


# add a user to the system
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && mkdir /home/$USERNAME/.config && chown $USER_UID:$USER_GID /home/$USERNAME/.config

RUN apt-get update \ 
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \ 
    && rm -rf /var/lib/apt/lists/*

# MUST INCLUDE -y in order to auto accept y/n when using apt-get to install gazebo, otherwise will abort
RUN sudo apt-get update \ 
    && apt-get install ros-${ROS_DISTRO}-xacro \
    && rm -rf /var/lib/apt/lists/*

RUN sudo apt-get update \ 
    && apt-get -y install ros-${ROS_DISTRO}-gazebo-ros-pkgs \ 
    && rm -rf /var/lib/apt/lists/*

# run the container as the user and not root, best practice to not do this
#USER ros

COPY entrypoint.sh /entrypoint.sh
COPY bashrc /home/${USERNAME}/.bashrc

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["bash"]

