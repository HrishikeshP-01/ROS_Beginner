#!/usr/bin/env python

# Make the tutle move in a straight line

import rospy
import time
from geometry_msgs.msg import Twist

pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
rospy.init_node('tutlesimDemo',anonymous=True)
move=Twist()

i=0
while i<=3:
	rospy.loginfo("Moving straight")
	move.linear.x=2
	pub.publish(move)
	i=i+1
	rospy.sleep(1)
rospy.loginfo("move stop")
move.linear.x=0
pub.publish(move)
