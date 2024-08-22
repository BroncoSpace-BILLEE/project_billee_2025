from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
        ),

        Node(
            package='joy',
            executable='joy_node',
        ),

        Node(
            package='manual_movement',
            executable='converter'
        )
    ])