# plot position: ekf odometry + imu 

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose


rospy.init_node('get_odom_ttb3')
pub_odom = rospy.Publisher('odom_ttb3',Pose,queue_size=10)

rate = rospy.Rate(1)

def callback(msg):
    odom_ttb3 = Pose()
    odom_ttb3.position.x = msg.pose.pose.position.x 
    odom_ttb3.position.y = msg.pose.pose.position.y - 0.25 #0.5 m1 0.25 m2 

    pub_odom.publish(odom_ttb3)

    print(f'Odom pose smb: {odom_ttb3.position.x:.3f} {odom_ttb3.position.y:.3f}')
    print('---------------')

sub = rospy.Subscriber('/odometry/filtered',Odometry,callback)

rospy.spin()