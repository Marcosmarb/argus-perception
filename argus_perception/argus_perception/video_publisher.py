from pathlib import Path

import cv2
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image


class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')

        self.declare_parameter('sequence_path', '')
        self.declare_parameter('fps', 30.0)
        self.declare_parameter('loop', True)
        self.declare_parameter('frame_id', 'camera')

        sequence_path = self.get_parameter('sequence_path').value
        fps = self.get_parameter('fps').value
        self.loop = self.get_parameter('loop').value
        self.frame_id = self.get_parameter('frame_id').value
        self.frames = sorted(Path(sequence_path).glob('*.jpg'))
        if not self.frames:
            self.get_logger().error(f'No .jpg frames found in "{sequence_path}"')
            raise SystemExit(1)

        self.bridge = CvBridge()
        self.index = 0
        self.publisher = self.create_publisher(Image, 'camera/image_raw', 10)
        self.create_timer(1.0 / fps, self.publish_frame)

        self.get_logger().info(f'Publishing {len(self.frames)} frames at {fps} FPS')

    def publish_frame(self):
        if self.index >= len(self.frames):
            if self.loop:
                self.index = 0
            else:
                return

        image = cv2.imread(str(self.frames[self.index]))
        msg = self.bridge.cv2_to_imgmsg(image, encoding='bgr8')
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.frame_id
        self.publisher.publish(msg)
        self.index += 1


def main():
    rclpy.init()
    node = VideoPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
