from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch the turtlesim simulator
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        # Launch your move_turtle node
        Node(
            package='ros2_move_turtle',
            executable='move_turtle_exec',
            name='move_turtle'
        ),
    ])
