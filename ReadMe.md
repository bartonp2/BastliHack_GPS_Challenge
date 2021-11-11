## GPS Challenge

To control the leorover we have already prepared the neccessary ROS packages for you which will handle the communication with the LeoRover. All you need to do is complete the navigation logic within the leo_navigation package.

1. Edit the code in: `~/catkin_ws/src/leo_navigation/scripts/leo_navigation_node.py`
2. Run the code with: `roslaunch leo_navigation leo_navigation.launch`

**Note**: You will need to set drive commands with a frequency of at least 2Hz. If the rover does not receive a command for 0.5s it will set the velocity to zero.

### Contents

1. **leo_navigation** - this is the package responsible for controlling the rover. Your navigation logic will go in the `leo_navigation/scripts/leo_navigation_node.py` file at the marked location
2. **leo_joy_example** - this is a package for controlling the rover with the joystick. You do not need make any changes here.

### Setup

* Make sure to connect to the leorovers hotspot  -  Password: bastlihack
* If ROS complains your ROS_IP is incorrect:
  * check your IP with `ip address` and search for your network interface and the `inet` keyword
  * Set your ROS_IP accordingly: `export ROS_IP=X.X.X.X` 
    * To have it set in every new shell edit the corresponding line at the bottom of the `~/.bashrc` file

##### Login Info

The raspberry pi is named `piberry` and `bastli` is the default user with password `bastlihack`.

### Additional Info

When running leo_navigation.launch this will automatically run the joystick controller in addition to your navigation code. The commands from your navigation code can be overriden at any time with the controller by holding down the `RB` button and using the joysticks to steer.

If you decide to use C++ or change the ROS messages you will need to build the workspace before running it with `catkin build`. When only using python you don't have to rebuild every time.
