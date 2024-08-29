import os
import sys
from ament_index_python.packages import get_package_share_directory
sys.path.append(os.path.join(get_package_share_directory('rm_vision_bringup'), 'launch'))

def generate_launch_description():

    from common import launch_params, robot_state_publisher, node_params, tracker_node
    from launch_ros.actions import Node
    from launch import LaunchDescription

    # 添加视频流节点
    video_publisher_node = Node(
        package='video_cam',  # 替换为你的视频发布节点所在的包名
        executable='video_publisher',   # 替换为视频发布节点的可执行文件名
        emulate_tty=True,
        output='screen',
        parameters=[{'video_file': '/home/lth/ros_ws/src/video_cam/video_cam/video.mp4'}],  # 如果你想通过参数指定视频路径
    )

    detector_node = Node(
        package='armor_detector',
        executable='armor_detector_node',
        emulate_tty=True,
        output='both',
        parameters=[node_params],
        arguments=['--ros-args', '--log-level',
                   'armor_detector:='+launch_params['detector_log_level']],
    )

    return LaunchDescription([
        robot_state_publisher,
        video_publisher_node,  # 加入视频发布节点
        detector_node,
        tracker_node,
    ])
