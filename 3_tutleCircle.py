#!/usr/bin/env python

# program to make the turtle move in a cirle
# logic is that a body moving with a uniform linear and angular vel. has to traverse in a circular path

import rospy
import time
from geometry_msgs.msg import Twist

pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
rospy.init_node('move_circle',anonymous=True)
move=Twist()

while not rospy.is_shutdown():
	rospy.loginfo('moving circular')
	move.linear.x = 2
	move.angular.z=2
	pub.publish(move)
	rospy.sleep(1)
rospy.loginfo('stop')
move.linear.x=0
move.angular.z=0
pub.publish(move)
