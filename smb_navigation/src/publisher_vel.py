# use teleop key control robot 

#!/usr/bin/env python3
import rospy 
from geometry_msgs.msg import Twist

class movement:
    def __init__(self):
        rospy.init_node('pub_move_robot', anonymous=False)
        self.pub_move = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
        self.move = Twist()
        
    def publish_vel(self):
        self.pub_move.publish(self.move)

    def move_forward(self):
        self.move.linear.x = 0.5
        self.move.angular.z = 0.0

    def move_lelf(self):
        self.move.linear.x = 0.0
        self.move.angular.z = 0.2
    
    def move_right(self):
        self.move.linear.x = 0.0
        self.move.angular.z = -0.2

    def stop(self):
        self.move.linear.x = 0.0
        self.move.angular.z = 0.0

    def move_backward(self):
        self.move.linear.x = -0.5
        self.move.angular.z = 0.0

    def pub_vel(self,li_x,li_y,li_z,an_x,an_y,an_z):
        self.move.linear.x = li_x
        self.move.linear.y = li_y
        self.move.linear.z = li_z
        self.move.angular.x = an_x
        self.move.angular.y = an_y
        self.move.angular.z = an_z


if __name__ == "__main__":
    mov = movement()
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        movement = input('Enter the direction:')

        if movement == 'w':
            mov.move_forward()

        if movement == 'a':
            mov.move_lelf()

        if movement == 's':
            mov.stop()

        if movement == 'd':
            mov.move_right()

        if movement == 'x':
            mov.move_backward()

        if movement == 'g':
            li_x, li_y, li_z = list(map(float,input("Enter the linear velocity:").split()))
            an_x, an_y, an_z = list(map(float,input("Enter the angular velocity:").split()))
            mov.pub_vel(li_x,li_y,li_z,an_x,an_y,an_z)

        mov.publish_vel()
        rate.sleep()