# find matrix transform from map->odom->base_link to get postion estimate from map by slam 

import rospy
import tf
from geometry_msgs.msg import Pose

rospy.init_node('tf_transform')
pub = rospy.Publisher('pose_estimate_smb',Pose,queue_size=10)
listener = tf.TransformListener()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    try:
        (trans1,rot1) = listener.lookupTransform("map","odom",rospy.Time(0))
        (trans2,rot2) = listener.lookupTransform("odom","base_link",rospy.Time(0))
        # print("{:.3f}".format(trans[0]))
        # print("{:.3f}".format(trans[1]))
        # print("{:.3f}".format(trans[2]))
        # print("---------")
        pose_smb = Pose()
        pose_smb.position.x = trans2[0] - trans1[0]
        pose_smb.position.y = trans2[1] - trans1[1]
        pub.publish(pose_smb)

    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        continue
    rate.sleep()
