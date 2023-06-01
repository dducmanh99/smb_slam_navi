# get position of pillar 

import rospy
from sensor_msgs.msg import LaserScan
from smb_navigation.msg import Pose

class pillar:
    def __init__(self):
        self.sub = rospy.Subscriber('/scan',LaserScan,self.callback)
        self.data = LaserScan()
        self.pub = rospy.Publisher('/pose_pillar',Pose,queue_size=10)
        self.pose_pillar = Pose()
    def callback(self,msg):
        self.data = msg
        self.sum = 0 
        self.count = 0
        for i in range(302):
            if (self.data.ranges[i]<50):
                self.sum = self.sum + i
                self.count = self.count + 1
        # Xac dinh truc cua cay cot nam o goc bao nhieu so voi robot
        self.central = int(int(self.sum / self.count) * 270 / 302) - 135
        self.dis = self.data.ranges[int(self.sum/self.count)]

        self.pose_pillar.oriantation = self.central
        self.pose_pillar.distance = self.dis
        self.pub.publish(self.pose_pillar)
        
        # In ra vi tri cua truc cay cot voi vi tri goc va khoang cach so voi robot
        print("pillar o goc: {}(do)".format(self.central)) 
        print("khoang cach den pillar:{}(m)".format(self.dis))
        print("-------------")


if __name__ == "__main__":
    rospy.init_node('find_pillar',anonymous=True)
    pil = pillar()
    rospy.spin()



# rospy.init_node('find_pillar')
# sub = rospy.Subscriber('/scan',LaserScan,callback)
# rospy.spin()