
import rclpy
import math
from rclpy.node import Node

from turtlesim.msg import Pose


class PoseControl(Node):

    def __init__(self):
        super().__init__('pose_control')
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.calculate_position,
            10)
        self.subscription  # prevent unused variable warning

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

    def calculate_position(self, pose):
        self.x = pose.x
        self.y = pose.y
        self.theta = pose.theta
        
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

