from setuptools import find_packages, setup

package_name = 'video_cam'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lth',
    maintainer_email='2284268273@qq.com',
    description='A ROS2 package for publishing video streams',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'video_publisher = video_cam.video_publisher:main',
        ],
    },
)
