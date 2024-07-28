# Intro to ROS: Nodes, Topics, and Services

**This doc is heavily condensed and should only serve as a primer for the following articles**

1. [*Using `turtlesim`, `ros2`, and `rqt`](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html)  
1. [*Understanding nodes*](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)  
1. [*Understanding topics*](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)  
1. [*Understanding services*](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)

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

> Note: these names are actually really bad in production for reasons I will get into later.

However, how does each node know what to listen to? The nodes that handle the movement of the rover don't need the camera footage, and vice versa. 

This is where **topics** come in.

## What is a "topic"?

A topic is exactly what it sounds like. It helps us sort the information that the nodes are passing to each other. A node can **publish** to a topic to send out information, and **subscribe** to a topic to listen/receive to information.

Publishers usually **continuously** send out information as a stream, and subscribers usually receive everything they can. 

![topic example gif](https://docs.ros.org/en/humble/_images/Nodes-TopicandService.gif)

### Topic Example: Homebase + Rover

We can create topics called `/controls` and `/cameras`.

Now the controls_publisher can publish to the `/controls topic`, and the `controls_subscriber` can subscribe to the /controls topic to listen for the controls.

The same can be done for the camera nodes. This is extremely useful when more and more nodes are added to the mix.

#### Subtopics Example: Homebase + Rover

Subtopics are topics that are within another topic. 

Imagine that we decide to add an arm to the rover. Now, the homebase needs to also be able to control the arm.

Since controlling the arm is still related to `/controls` but is not related to the controls for the movement, we can create the subtopics `/controls/arm` and `/controls/movement` to differentiate the two. We can then create the required nodes on the rover and homebase.

> Note: Now, we have to rename the controls_subscriber and controls_publisher nodes.

## What is a "service"?

A service is another way nodes can communicate with each other. Services are based on **calls** and **responses**.

Compared to topics, services are more “precise” with the information they send. A **client node** can **call** a service, and a **server node** will respond to that specific client. 

- With topics, all subscribers can receive information from all publishers

The server node will also only send out information if it receives a call from another client node.

- With topics, all publishers continuously send out information regardless if there are any subscribers.

![Service example gif](https://docs.ros.org/en/humble/_images/Service-MultipleServiceClient.gif)

### Service Example: Homebase + Rover

Imagine now we need to implement a form of autonomous navigation. We send the rover a GPS coordinate, and the rover should move to that location, then tell us when it reaches its destination.

To do this, we can create a service called `/gps_nav`, where the rover is the server, and the homebase is the client.

The client will then call the `/gps_nav` service with the coordinates as parameters, and the rover should move accordingly. Once the rover reaches the destination, it should respond to the homebase with a status message.

> Note: Some services can actually have empty calls and responses. Sometimes we just need the service to activate a process on the server, and the client doesn’t care about a response.
