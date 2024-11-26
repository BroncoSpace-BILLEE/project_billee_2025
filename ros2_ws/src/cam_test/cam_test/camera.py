import cv2
import numpy as np
from cv_bridge import CvBridge

class Camera:

    def __init__(self, usb_port:int):
        self.usb_port = usb_port

        self.frame_width = 320
        self.frame_height = 240
        self.fps = 30
        self.num_img_chunks = 3
        self.cap = None
        self.bridge = CvBridge()

    def start_cap(self):
        if self.cap is not None:
            print('Video Capture Already Started')
            return

        self.cap = cv2.VideoCapture(self.usb_port)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
        self.cap.set(cv2.CAP_PROP_FPS, self.fps)

        print(f'Started Capture for port {self.usb_port}')


    def edit_output_params(self, settings:dict):

        if settings:
            self.frame_width = settings.get('frame_width', self.frame_width)
            self.frame_height = settings.get('frame_height', self.frame_height)
            self.fps = settings.get('fps', self.fps)

            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
            self.cap.set(cv2.CAP_PROP_FPS, self.fps)

        
        return

    def cap_opened(self)->bool:
        return self.cap.isOpened()

    def get_frame(self):
        return self.cap.read()

    def get_compressed_data(self) -> list:
        # surround in try/catch later

        ret, frame = self.get_frame()

        if not ret:
            return None

        compressed_data = self.bridge.cv2_to_compressed_imgmsg(frame, 'jpg').data
        img_data = np.asarray(compressed_data, dtype=np.uint8)

        split_data = np.array_split(img_data, self.num_img_chunks)

        return split_data

    def destroy_cap(self):
        self.cap.release()
        print(f'released capture feed for camera on port {self.usb_port}')
        self.cap = None


