import cv2
import cv2
print(cv2.__version__)

cap = cv2.VideoCapture('/home/lth/ros_ws/src/video_cam/video_cam/video.mp4')
if cap.isOpened():
    print("Video file opened successfully.")
else:
    print("Cannot open video file.")
