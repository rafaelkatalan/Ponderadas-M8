from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
    ExecuteProcess(
        cmd=['ros2', 'launch', 'webots_ros2_turtlebot', 'robot_launch.py'],
        output='screen',
    ),
    ExecuteProcess(
        cmd=['ros2', 'launch', 'nav2_bringup', 'tb3_simulation_launch.py', 'slam:=True'],
        output='screen',
    ),
    ExecuteProcess(
        cmd=['python3', 'launch_move.py'],
        output='screen',
    )
    ])

if __name__ == '__main__':
    generate_launch_description()
