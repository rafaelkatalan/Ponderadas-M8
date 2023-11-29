import rclpy
from rclpy.node import Node
from unidecode import unidecode
from std_msgs.msg import String


class ChatPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'chat', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = unidecode(str(input()))
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

class ChatSubscriber(Node):
    
        def __init__(self):
            super().__init__('minimal_subscriber')
            self.subscription = self.create_subscription(
                String,
                'chat2',
                self.listener_callback,
                10)
            self.subscription  # prevent unused variable warning
    
        def listener_callback(self, msg):
            print(msg.data)
            self.get_logger().info('I heard: "%s"' % msg.data)



def main(args=None):
    
    rclpy.init(args=args)
    minimal_publisher = ChatPublisher()
    minimal_subscriber = ChatSubscriber()
    rclpy.spin(minimal_publisher)
    rclpy.spin(minimal_subscriber)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()