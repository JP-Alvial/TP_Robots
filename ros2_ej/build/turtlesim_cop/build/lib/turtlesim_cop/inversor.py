
import rclpy
import math
from rclpy.node import Node

from turtlesim.msg import Pose
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist

class InvertCtrl(Node):

    def __init__(self):
        super().__init__('invert_control')

        self.vel = Twist()

        self.vel.linear.x = 0.0
        self.vel.angular.z = 0.0
        self.init = False

        self.get_init = self.create_subscription(
            Float64MultiArray,
            'init',
            self.iniciate,
            4)
        self.get_init  # prevent unused variable warning

        self.get_data = self.create_subscription(
            Twist,
            'turtle1/cmd_vel',
            self.invert,
            20)
        self.get_data  # prevent unused variable warning

        self.pub_vel = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)

    def invert(self, msg):
        self.vel.linear.x = - msg.linear.x
        self.vel.angular.z = - msg.angular.z

        self.pub_vel.publish(self.vel)
        
    def iniciate(self, msg):
        self.x_obj = msg.data[0]
        self.y_obj = msg.data[1]
        self.init = True

def main(args=None):
    rclpy.init(args=args)

    invert_control = InvertCtrl()

    rclpy.spin(invert_control)

    invert_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

