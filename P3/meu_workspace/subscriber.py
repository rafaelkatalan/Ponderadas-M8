import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import re

from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from math import pi

import subprocess

def gotop0():
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, pi/4)
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = BasicNavigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = 1.0
    goal_pose.pose.position.y = 0.0
    goal_pose.pose.position.z = 0.0
    goal_pose.pose.orientation.x = q_x
    goal_pose.pose.orientation.y = q_y
    goal_pose.pose.orientation.z = q_z
    goal_pose.pose.orientation.w = q_w

    BasicNavigator.goToPose(goal_pose)
    while not BasicNavigator.isTaskComplete():
        print(BasicNavigator.getFeedback())

def create_pose_stamped(navigator, pos_x, pos_y, rot_z):
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, rot_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = BasicNavigator.get_clock().now().to_msg()
    pose.pose.position.x = pos_x
    pose.pose.position.y = pos_y
    pose.pose.position.z = pos_x
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose

locais = {'secretaria':(0.0, 0.0), 'laboratorio':(1.0, 1.0), 'biblioteca':(2.0, 2.0)}
padrao = re.compile(r"(?:V[áa] para|Dir[íi]ja-se [àa]o|Me leve para) (?:[ao] )?(\w+)", flags=re.IGNORECASE | re.UNICODE)

class ChatSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String, 'chat', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        texto = padrao.search(msg.data)
        try:
            local = texto.group(1)
            if local in locais:
                pose_x = locais[local][0]
                pose_y = locais[local][1]
                goal_pose = create_pose_stamped(BasicNavigator, pose_x, pose_y, 1.57)
                BasicNavigator.goToPose(goal_pose)
                while not BasicNavigator.isTaskComplete():
                    print(BasicNavigator.getFeedback())
            else:
                print("Local nao encontrado")
        except():
            print("Comando nao reconhecido")


def main(args=None):
    subprocess.Popen(["xterm", "-e", "python3", "publisher.py", "2>&1"], stderr=subprocess.STDOUT)
    rclpy.init(args=args)
    #gotop0()
    minimal_subscriber = ChatSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()