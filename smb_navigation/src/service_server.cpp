#include<ros/ros.h>
#include<std_srvs/SetBool.h>

bool cur_rb = false;

bool changes_state_robot(std_srvs::SetBool::Request &req, std_srvs::SetBool::Response &res){
    if (req.data == 0){
        if(cur_rb==0){
            res.success = 1;
            res.message = "Robot is already stopped";
        }
        else{
            cur_rb = 0;
            res.success = 0;
            res.message = "Stopping robot";
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
        }
    }
    return true;
}

int main(int argc, char **argv){
    ros::init(argc, argv, "changes_state_robot_server");
    ros:: NodeHandle srv;

    ros::ServiceServer service = srv.advertiseService("changes_state_robot",changes_state_robot);

    ros::spin();
    
    return 0;
}