import geometry_msgs.msg
import rclpy
from rclpy.node import Node

import rclpy.topic_endpoint_info
import sensor_msgs
import geometry_msgs
import sensor_msgs.msg

class Converter(Node):

    def __init__(self):
        super().__init__('converter')
        self.subscription = self.create_subscription(
            msg_type=sensor_msgs.msg.Joy,
            topic='/joy',
            callback=self.sub_callback,
            qos_profile=10,
        )
        self.publisher = self.create_publisher(
            msg_type=geometry_msgs.msg.Twist,
            topic='/turtle1/cmd_vel',
            qos_profile=10,
        )
        

    def sub_callback(self, msg):
        lol = geometry_msgs.msg.Twist()
        lol.angular.x = 0.0
        lol.angular.y = 0.0
        lol.angular.z = 0.0

        lol.linear.x = -msg.axes[0]
        lol.linear.y = msg.axes[1]
        lol.linear.z = 0.0

        self.publisher.publish(lol)

def main(args=None):
    rclpy.init(args=args)

    node = Converter()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

