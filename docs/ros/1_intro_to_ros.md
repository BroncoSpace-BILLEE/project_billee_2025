# Intro to ROS: Nodes, Topics, and Services

ROS stands for Robot Operating System. It is not actually an OS, but rather a framework for developing software for robotics.
For our project, we will be using ROS2 Humble.

## Thought process behind ROS

ROS encourages the developer to create many "nodes" that each have their own separate responsibilities. These nodes can talk to each other through "topics" and "services" to accomplish complex tasks.

## What is a "node"?

A node is really just a program that we write. However, in the context of ROS, we call it a node.

### Node Example: Homebase + Rover

Imagine we have a rover and a base station. We need to implement the following features: 
1. Controlling the rover's movement from homebase.
2. Viewing the cameras on the rover from homebase.

To implement movement, we can create a node on homebase to send out our controls called `controls_publisher`. On the rover, we can create a node to listen to the controls called `controls_subscriber`.

To implement the camera feed, we can do a something similar. We create a node on the rover called `camera_publisher` and a node on homebase to listen to the footage called `camera_subscriber`.

>> Note: these names are actually really bad in production for reasons I will get into later.

However, how does each node know what to listen to? The nodes that handle the movement of the rover don't need the camera footage, and vice versa. 

This is where **topics** come in.

## What is a "topic"?

A topic is exactly what it sounds like. It helps us sort the information that the nodes are passing to each other. A node can **publish** to a topic to send out information, and **subscribe** to a topic to listen/receive to information.

Publishers usually **continuously** send out information as a stream, and subscribers usually receive everything they can. 

![](https://docs.ros.org/en/humble/_images/Nodes-TopicandService.gif)

### Topic Example: Homebase + Rover

We can create topics called `/controls` and `/cameras`.

Now the controls_publisher can publish to the `/controls topic`, and the `controls_subscriber` can subscribe to the /controls topic to listen for the controls.

The same can be done for the camera nodes. This is extremely useful when more and more nodes are added to the mix.

#### Subtopics Example: Homebase + Rover

Subtopics are topics that are within another topic. 

Imagine that we decide to add an arm to the rover. Now, the homebase needs to also be able to control the arm.

Since controlling the arm is still related to `/controls` but is not related to the controls for the movement, we can create the subtopics `/controls/arm` and `/controls/movement` to differentiate the two. We can then create the required nodes on the rover and homebase.

*Note: Now, we have to rename the controls_subscriber and controls_publisher nodes.
