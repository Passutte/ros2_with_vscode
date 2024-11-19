from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_pubsub',
            namespace='',
            executable='talker',
            name='sim'
        ),
    ])