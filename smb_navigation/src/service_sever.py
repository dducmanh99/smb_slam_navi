#!/usr/bin/env python3
import rospy 
from smb_navigation.srv import robot_state, robot_stateResponse

def callback(request):
    return robot_stateRes(request.data)

def changes_state():
    rospy.init_node("changes_state_service")
    service = rospy.Service("changes_state",robot_state,callback)
    rospy.spin()

if __name__ == "__main__":
    changes_state()