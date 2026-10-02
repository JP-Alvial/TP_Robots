
import rclpy
import math
from rclpy.node import Node

from turtlesim.msg import Pose
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist

class PoseControl(Node):

    def __init__(self):
        super().__init__('pose_control')

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.x_obj = 0.0
        self.y_obj = 0.0
        self.theta_obj = 0.0
        self.init = False
        self.timer_period = 0.1

        self.get_init = self.create_subscription(
            Float64MultiArray,
            'init',
            self.iniciate,
            4)
        self.get_init  # prevent unused variable warning

        self.get_data = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.put_pos,
            50)
        self.get_data  # prevent unused variable warning

        self.pub_vel = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(self.timer_period, self.timer_main)


    def put_pos(self, pose):
        self.x = pose.x
        self.y = pose.y
        self.theta = pose.theta
        
    def iniciate(self, msg):
        self.x_obj = msg.data[0]
        self.y_obj = msg.data[1]
        self.init = True

    def timer_main(self):

        if not self.init:
            return

        prox = 0.1
        vel = Twist()

        dx = self.x_obj - self.x
        dy = self.y_obj - self.y
        dist_dif = math.sqrt(dx**2 + dy**2)

        theta_obj = math.atan2(dy, dx)
        theta_dif = theta_obj - self.theta
        theta_dif = math.atan2(math.sin(theta_dif), math.cos(theta_dif))

        if dist_dif < prox:
            vel.linear.x = 0.0
            vel.angular.z = 0.0
            self.init = False

        elif abs(theta_dif) > prox:
            vel.linear.x = 0.0
            vel.angular.z = max(-2.0, min(theta_dif * 2.0, 2.0)) 
        else:
            vel.angular.z = 0.0
            vel.linear.x = min(dist_dif * 1.0, 2.0)

        self.pub_vel.publish(vel)

def main(args=None):
    rclpy.init(args=args)

    pose_control = PoseControl()

    rclpy.spin(pose_control)

    pose_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

