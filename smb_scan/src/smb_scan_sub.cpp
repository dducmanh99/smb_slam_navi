#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"

void chatterCallback(const sensor_msgs::LaserScan::ConstPtr& msg)
{
    ROS_INFO("range_min: [%f]",msg->range_min);
}

int main(int argc, char **argv)
{
    ros::init(argc,argv,"smb_scan_sub");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("scan",1000,chatterCallback);
    ros::spin();
    return 0;
}