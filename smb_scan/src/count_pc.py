# this code counts numbers of point cloud 

import rospy
from sensor_msgs.msg import PointCloud2

def callback(msg):
    print("height of pc")
    print(msg.height)
    print("width of pc")
    print(msg.width)
    file = open("/home/manh/Documents/doan1/cmd.txt", "a")
    file.write("{}\n".format(msg.height))
    file.close()

rospy.init_node('num_pc')
sub = rospy.Subscriber('rslidar_points',PointCloud2,callback)
rospy.spin()