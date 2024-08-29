import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Image, 'video_frames', 10)
        self.timer = self.create_timer(0.033, self.timer_callback)  # 30 FPS
        
        # 指定视频文件的路径
        self.cap = cv2.VideoCapture('/home/lth/桌面/video.mp4')
        
        # 检查视频文件是否成功打开
        if not self.cap.isOpened():
            self.get_logger().error('Cannot open video file')
            rclpy.shutdown()

        self.bridge = CvBridge()

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            # 将帧转换为ROS Image消息
            msg = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
            self.publisher_.publish(msg)
        else:
            self.get_logger().info('Video file is finished or cannot be read.')
            self.cap.release()

def main(args=None):
    rclpy.init(args=args)
    video_publisher = VideoPublisher()
    rclpy.spin(video_publisher)
    video_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
