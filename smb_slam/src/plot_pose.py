# plot position of robot : real , estimate 

import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Pose

import tf
import numpy as np 
import math

rospy.init_node('get_pose_ttb3')
pub_real = rospy.Publisher('real_ttb3',Pose,queue_size=10)
pub_esti = rospy.Publisher('esti_ttb3',Pose,queue_size=10)
listener = tf.TransformListener()
rate = rospy.Rate(1)
count = 0

def callback(msg):

    (trans1,rot1) = listener.lookupTransform("map","odom",rospy.Time(0))
    (trans2,rot2) = listener.lookupTransform("odom","base_footprint",rospy.Time(0))
    esti_ttb3 = Pose()
    yall1 = math.atan2(2*(rot1[3]*rot1[2]),rot1[3]*rot1[3] - rot1[2]*rot1[2])
    yall2 = math.atan2(2*(rot2[3]*rot2[2]),rot2[3]*rot2[3] - rot2[2]*rot2[2])
    
    # array1 = np.array([[math.cos(yall2),-math.sin(yall2),0,],
    #               [math.sin(yall2),math.cos(yall2),0],
    #               [0,0,1]])
    array2 = np.array([[trans2[0]],
                    [trans2[1]],
                    [trans2[2]]])
    array3 = np.array([[math.cos(yall1),-math.sin(yall1),0],
                  [math.sin(yall1),math.cos(yall1),0],
                  [0,0,1]])
    array4 = np.array([[trans1[0]],
                    [trans1[1]],
                    [trans1[2]]])

    array5 = np.matmul(array3,array2)
    # array6 = np.matmul(array3,array4)
    esti_arr = np.add(array5,array4)

    real_ttb3 = Pose()
    real_ttb3.position.x = msg.pose[2].position.x
    real_ttb3.position.y = msg.pose[2].position.y #4 2 s
    

    


    # real_smb.position.x = real_smb.position.x + 6
    # real_smb.position.y = real_smb.position.y + 1.5
    esti_ttb3.position.x = esti_arr[0]
    esti_ttb3.position.y = esti_arr[1]

    pub_real.publish(real_ttb3)
    pub_esti.publish(esti_ttb3)
    # file_real_x = open("/home/manh/Documents/doan1/gmapping/real_x.txt","a")
    # file_real_x.write("{}\n".format(real_smb.position.x))
    # file_real_x.close()

    # file_real_y = open("/home/manh/Documents/doan1/gmapping/real_y.txt","a")
    # file_real_y.write("{}\n".format(real_smb.position.y))
    # file_real_y.close()

    # file_esti_x = open("/home/manh/Documents/doan1/gmapping/esti_x.txt","a")
    # file_esti_x.write("{}\n".format(esti_smb.position.x))
    # file_esti_x.close()

    # file_esti_y = open("/home/manh/Documents/doan1/gmapping/esti_y.txt","a")
    # file_esti_y.write("{}\n".format(esti_smb.position.y))
    # file_esti_y.close()
    print(f'Real pose smb: {real_ttb3.position.x:.3f} {real_ttb3.position.y:.3f}')
    print(f'Esti pose smb: {esti_arr[0]} {esti_arr[1]}')
    # print(f'yall_map2odom:  {yall1:.3f}')
    # print(f'yall_odom2base: {yall2:.3f}')
    print("---------------------")

sub = rospy.Subscriber('/gazebo/model_states',ModelStates,callback)

rospy.spin()

