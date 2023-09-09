
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class listener(Node):

    def __init__(self):
        super().__init__('listener_py')
        self.subscription = self.create_subscription(
            String,
            'new_message',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        print(" > %s" % msg.data)


def main(args=None):

    rclpy.init(args=args)
    myLis = listener()

    rclpy.spin(myLis)

    myLis.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()