
import rclpy
import math
from rclpy.node import Node

from turtlesim.msg import Pose


class PoseControl(Node):

    def __init__(self):
        super().__init__('pose_control')
        self.get_init = self.create_subscription(
            Pose,
            'init',
            self.iniciate,
            4)
        self.get_init  # prevent unused variable warning

        self.get_data = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.put_pos,
            10)
        self.get_data  # prevent unused variable warning

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

    def put_pos(self, pose):
        self.x = pose.x
        self.y = pose.y
        self.theta = pose.theta
        
        
    def iniciate(self, data):
        if data.x < 2.0:
            self.get_logger().info('I heard x: "%f"' % self.x)
            self.get_logger().info('I heard y: "%f"' % self.y)
            self.get_logger().info('I heard theta: "%f"' % self.theta)



def main(args=None):
    rclpy.init(args=args)

    pose_control = PoseControl()

    rclpy.spin(pose_control)

    pose_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

