#!/usr/bin/env python

# program to make the turtle move in a square

import rospy
import time
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
rospy.init_node('turtlesimdemo',anonymous = True)
move = Twist()

side=1
speed=1
aspeed=1
t0 = rospy.Time.now().to_sec()
pi=3.14

while not rospy.is_shutdown():
	dt0=rospy.Time.now().to_sec()
	dist=0
	move.linear.x=speed
	move.angular.z=0
	while(dist<side):
		pub.publish(move)
		dt1 = rospy.Time.now().to_sec()
		dist=speed*(dt1-dt0)
		rospy.loginfo("moving")
	move.linear.x=0
	pub.publish(move)
	at0=rospy.Time.now().to_sec()
	angle=0
	move.angular.z=aspeed
	while(angle<pi/2):
		pub.publish(move)
		at1= rospy.Time.now().to_sec()
		angle=aspeed*(at1-at0)
		rospy.loginfo("turning")
	
