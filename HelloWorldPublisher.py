#!/usr/bin/env python
# the script is executed as Python script

#importing libraries
import rospy # for rosnode
import time
from std_msgs.msg import String

pub=rospy.Publisher("Chatter",String,queue_size=10)
# pub is a Publisher publishing string msgs to Chatter and its queue size is 10

rospy.init_node("talker",anonymous=True)
# name of the node is talker. Only by setting the name can ROS Master know which node this is
# anonymous=True ensures the node name is unique by adding random no:s at end of the name

rate=rospy.Rate(10) 
# 10Hz
# Rate object created which decides how fast the loop must run in a sec - 10 times here

while not rospy.is_shutdown():
	hello_str="Hello World %s"% rospy.get_time()
	rospy.loginfo(hello_str)
	# loginfo does triple duty
	# 1- publish to terminal
	# 2 - write to log file
	# 3 - gets written to rosout which can be used for debugging
	pub.publish(hello_str)
	rate.sleep()
