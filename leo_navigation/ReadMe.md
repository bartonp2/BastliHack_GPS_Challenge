## GPS Challenge

To control the leorover we have already prepared the neccessary ROS package for you which will handle the communication with the LeoRover. All you need to do is complete the navigation logic within the leo_navigation package.

1. Edit the code in: ~/catkin_ws/src/leo_navigation/scripts/leo_navigation_node.py
2. Run the code with: rosrun leo_navigation leo_navigation_node.py

**Note**: You will need to set drive commands with a frequency of at least 2Hz. If the rover does not receive a command for 0.5s it will set the velocity to zero.
### Setup

* Make sure to connect to the leorovers wifi  -  Password: bastlihack
* If ROS complains your ROS_IP is incorrect:
  * check your IP with `ip address` and search for your network interface and the `inet` keyword
  * Set your ROS_IP accordingly: `export ROS_IP=X.X.X.X` 
    * To have it set in every new shell edit the corresponding line at the bottom of the `~/.bashrc` file

### Login Info

The raspberry pi is named `piberry` and `bastli` is the default user with password `bastlihack`.

