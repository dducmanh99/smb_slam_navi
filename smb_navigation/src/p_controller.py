# use P controller to move robot to pillar and visual pillar by marker 

#!/usr/bin/env python3
import rospy 
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan 
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point


class controller:
    def __init__(self):
        rospy.init_node('controller', anonymous=False)
        self.sub = rospy.Subscriber('/scan',LaserScan,self.callback)
        self.data = LaserScan()
        self.pub_move = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        self.move = Twist()

        #marker
        self.marker_objectlisher = rospy.Publisher('/marker_basic',Marker,queue_size=1)
        self.marker_object = Marker()
        
    def callback(self,msg):
        self.data = msg
        self.sum_ang = 0
        self.sum_dis = 0 
        self.count = 0 
        for i in range(302):
            if (self.data.ranges[i]<50):
                self.sum_ang = self.sum_ang + i
                self.sum_dis = self.sum_dis + self.data.ranges[i]
                self.count = self.count + 1
        self.ang = float(float(self.sum_ang / self.count) * 270 / 362) - 135
        self.dis = float(self.sum_dis/self.count)
        print("pillar o goc: {}(do)".format(self.ang)) 
        print("khoang cach den pillar:{}(m)".format(self.dis))
        print("-------------")
        self.kp = 0.05
        if self.dis < 5: 
            self.move.linear.x = 0
        else:
            self.move.linear.x = self.kp * self.dis

        if abs(self.ang) < 1:
            self.move.angular.z = 0
        else:
            self.move.angular.z = self.kp * self.ang
        
        self.pub_move.publish(self.move)
        print("li_x: {}".format(self.move.linear.x))
        print("an_x: {}".format(self.move.angular.z))
        print("===========================")
        
        #marker
        self.marker_object.header.frame_id = "base_inertia"
        self.marker_object.header.stamp = rospy.Time.now()
        self.marker_object.id = 0 
        self.marker_object.type = Marker.CYLINDER

        self.marker_object.pose.position.x= self.dis * math.cos(self.ang * 3.14/180)
        self.marker_object.pose.position.y= self.dis * math.sin(self.ang * 3.14/180)
        self.marker_object.pose.position.z=0
        self.marker_object.pose.orientation.x = 0.0
        self.marker_object.pose.orientation.y = 0.0
        self.marker_object.pose.orientation.z = 0.0
        self.marker_object.pose.orientation.w = 1.0

        self.marker_object.scale.x = 0.3
        self.marker_object.scale.y = 0.3
        self.marker_object.scale.z = 1.0

        self.marker_object.color.r = 0.0
        self.marker_object.color.g = 0.0
        self.marker_object.color.b = 1.0
        self.marker_object.color.a = 1.0

        self.marker_object.lifetime = rospy.Duration(0)

        self.marker_objectlisher.publish(self.marker_object)
    # def init_marker(self,index=0,z_val=0):
    #     self.marker_object = Marker()
    #     self.marker_object.header.frame_id = "base_inertia"
    #     self.marker_object.header.stamp = rospy.Time.now()
    #     self.marker_object.id = index 
    #     self.marker_object.type = Marker.CYLINDER

    #     my_point = Point()
    #     my_point.z = z_val
    #     self.marker_object.pose.position = my_point

    #     self.marker_object.pose.position.x= self.dis * math.cos(self.ang/180*3.14)
    #     self.marker_object.pose.position.y= self.dis * math.sin(self.ang/180*3.14)
    #     self.marker_object.pose.position.z=0
    #     self.marker_object.pose.orientation.x = 0.0
    #     self.marker_object.pose.orientation.y = 0.0
    #     self.marker_object.pose.orientation.z = 0.0
    #     self.marker_object.pose.orientation.w = 1.0

    #     self.marker_object.scale.x = 1.0
    #     self.marker_object.scale.y = 1.0
    #     self.marker_object.scale.z = 1.0

    #     self.marker_object.color.r = 0.0
    #     self.marker_object.color.g = 0.0
    #     self.marker_object.color.b = 1.0
    #     self.marker_object.color.a = 1.0

    #     self.marker_object.lifetime = rospy.Duration(0)

    #     self.marker_objectlisher.publish(self.marker_object)

if __name__ == "__main__":
    while not rospy.is_shutdown():
        ctl = controller()
        rospy.rostime.wallsleep(1.0)
