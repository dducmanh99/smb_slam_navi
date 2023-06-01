cmake_minimum_required(VERSION 3.0.2)
project(smb_slam)

################################################################################
# Find catkin packages and libraries for catkin and system dependencies
################################################################################
find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  sensor_msgs
  gazebo_msgs
  tf
  geometry_msgs
  nav_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp sensor_msgs  
)

install(DIRECTORY bag config launch rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS src/plot_pose.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_install_python(PROGRAMS src/transform.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_install_python(PROGRAMS src/plot_ekf.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)