#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


# Initialize ROS node
rospy.init_node("leo_nav_node")

# Create ROS publisher
cmd_pub = rospy.Publisher("nav_vel", Twist, queue_size=1)
rospy.sleep(1.0) # Wait for ros initilisation to finish

def drive(linear: float, angular: float) -> None:
    """ Use this function to command the rover

    :param linear: linear speed in m/s
    :param angular: angular speed in rad/s
    """
    
    # Initialize ROS message object
    twist = Twist()
    twist.linear.x = linear
    twist.angular.z = angular

    cmd_pub.publish(twist) # publish message to the rover


def safe_exit():
    """ Publish zero velocity command before finishing the script """
    drive(0, 0)


# =============== Todo: Your code goes here =============================================
def main():
    # For example: Drive forward for 2s, then stop
    drive(0.2, 0.0)
    rospy.sleep(2) # sleep for 2s
    drive(0.0, 0.0)

# =============== Your code stops here ==================================================


if __name__ == '__main__':
    try:
        main()
    finally:
        safe_exit()
