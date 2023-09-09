import rclpy
from rclpy.node import Node

from std_msgs.msg import String    


class talker(Node):

    def __init__(self,user_name):
        super().__init__('talker_py')
        self.publisher_ = self.create_publisher(String, 'new_message', 10)
        self.username = user_name
        timer_period = 0.1
        self.timer = self.create_timer(timer_period,self.talker_callback)


    def talker_callback(self):
        msg = String()
        message = input()
        msg.data = self.username + " : " + message
        self.publisher_.publish(msg)



def main(args = None):

    user = input("enter your username: ")


    rclpy.init(args = args)
    myTalk = talker(user_name= user)

    rclpy.spin(myTalk)

    myTalk.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()