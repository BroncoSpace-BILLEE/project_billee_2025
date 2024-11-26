from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():


    camera_node_1 = Node(
            package='usb_cam_test', 
            executable='cam_streamer',
            name = 'cam_1_node',
            parameters=[{'usb_port': 2, 'port': 8080}],
            )

    return LaunchDescription([
        camera_node_1
    ])
