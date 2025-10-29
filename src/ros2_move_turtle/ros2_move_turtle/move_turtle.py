import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class MoveTurtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.current_pose = None
        self.stop = False
        self.timer = self.create_timer(0.1, self.move)

    def pose_callback(self, msg):
        self.current_pose = msg
        if msg.x > 17.0 or msg.y > 17.0:
            self.get_logger().info("Boundary reached → stopping turtle")
            self.stop = True

    def move(self):
        if self.current_pose is None:
            return
        
        twist = Twist()
        if not self.stop:
            twist.linear.x = 1.0
            twist.angular.z = 0.5
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
