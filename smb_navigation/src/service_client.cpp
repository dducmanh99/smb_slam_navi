#include<ros/ros.h>
#include<std_srvs/SetBool.h>
#include<geometry_msgs/Twist.h>

bool cur_rb;
ros::Publisher pub;
ros::Subscriber sub;

void callback(const geometry_msgs::Twist msg){
    if(msg.linear.x == 0 && msg.angular.z == 0){
        cur_rb = 0;
    }
    else{
        cur_rb = 1;
    }
}

bool changes_state_robot(std_srvs::SetBool::Request &req, std_srvs::SetBool::Response &res){
    geometry_msgs::Twist vel;
    if (req.data == 0){
        if(cur_rb==0){
            res.success = 1;
            res.message = "Robot is already stopped";
        }
        else{
            cur_rb = 0;
            res.success = 0;
            res.message = "Stopping robot";
            vel.linear.x = 0.0;
            vel.angular.z = 0.0;
        }
    }
    else{
        if(cur_rb==1){
            res.success = 1;
            res.message = "Robot is already running";
        }
        else{
            cur_rb = 1;
            res.success = 0;
            res.message = "Starting robot";
            vel.linear.x = 0.5;
            vel.angular.z = 0.0;
        }
    }
    pub.publish(vel);
    return true;
}

int main(int argc, char **argv){
    ros::init(argc, argv,"changes_state_robot_server");
    ros::NodeHandle srv;
    
    ros::ServiceServer service = srv.advertiseService("changes_state_robot",changes_state_robot);

    pub = srv.advertise<geometry_msgs::Twist>("cmd_vel",1000);
    sub = srv.subscribe("cmd_vel",1000,callback);

    ros::spin();
    return 0;
}