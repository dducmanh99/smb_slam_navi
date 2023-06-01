# 

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    sum = 0 
    count = 0
    for i in range(302):
        if (msg.ranges[i]<50):
            sum = sum + i
            count = count + 1
    # Xac dinh truc cua cay cot nam o goc bao nhieu so voi robot
    central = int(int(sum / count) * 270 / 302) - 135
    # In ra vi tri cua truc cay cot voi vi tri goc va khoang cach so voi robot
    print("pillar o goc: {}(do)".format(central)) 
    print("khoang cach den pillar:{}(m)".format(msg.ranges[int(sum/count)]))
    
rospy.init_node('scan_value')
sub = rospy.Subscriber('scan',LaserScan,callback)
rospy.spin()