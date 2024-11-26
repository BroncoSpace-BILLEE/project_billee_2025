import socket
import signal

import time
import sys

import argparse

import rclpy
from rclpy.node import Node
from cam_test.camera import Camera


class CameraPublisher(Node):


    def __init__(self):
        super().__init__('cam_streamer')

        
        #self.declare_parameter('usb_port', 1) #camera usb port
        #self.declare_parameter('port', 4096)

        #usb_port = self.get_parameter('usb_port').value
        #port = self.get_parameter('port').value

        usb_port = 2
        port = 8080

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', port)
        self.server_socket.bind(server_address)

        print(f'Started server at port {port}')

        self.camera = Camera(usb_port)
        self.camera.start_cap()

        if not self.camera.cap_opened():
            print(f"Failed to open camera at usb port {usb_port}")

        self.timer = self.create_timer(1/30, self.timer_callback) #run at every 1/30th of a second

    
    def timeout_handler(self, signum, frame):
        self.camera.destroy_cap()
        raise TimeoutError()

    
    def timer_callback(self):


        #surround in try/catch later

        print(f'Sending Data!')
        data, address = self.server_socket.recvfrom(4096)

        split_data = self.camera.get_compressed_data()

        self.server_socket.sendto(split_data[0].tobytes(), address)
        self.server_socket.recvfrom(4096)

        self.server_socket.sendto(split_data[1].tobytes(), address)
        self.server_socket.recvfrom(4096)

        self.server_socket.sendto(split_data[2].tobytes(), address)
        self.server_socket.recvfrom(4096)

        print(f'Sent frame from usb camera {self.usb_port}')

    

def main(args=None):
    rclpy.init(args=args)

    cam_streamer = CameraPublisher()
    rclpy.spin(cam_streamer)

    cam_streamer.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

