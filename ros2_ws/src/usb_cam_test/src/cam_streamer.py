import socket
import signal
import time
import sys
import argparse
import rclpy
from rclpy.node import Node
from camera import Camera


class CameraStreamer(Node):


    def __init__(self):
        super().__init__('camera')

        
        self.declare_parameter('usb_port', 1) #camera usb port
        self.declare_parameter('port', 4096)

        usb_port = self.get_parameter('usb_port').value
        port = self.get_parameter('port').value

        self.server.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address - ('192.168.1.11', port) #localhost
        self.server_socket.bind(server_address)

        print(f'Started server at port {port}')

        self.camera = Camera(usb_port)
        self.camera.start_cap()

        if not self.camera.cap_opened():
            print(f"Failed to open camera at usb port {usb_port}")

        self.timer = self.create_timer(1/30, self.timer_callback) #run at every 1/30th of a second

    
    def timeout_handler(self, signum, frame)
        raise TimeoutError()

    



