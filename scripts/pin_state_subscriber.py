#!/usr/bin/env python3
import rospy
import RPi.GPIO as GPIO

def pin_state_callback(msg):
	pass

if __name__ == '__main__':
	rospy.init_node("pin_state_subscriber')
	
	rospy.Subscriber('pin_state', Bool, pin_state_callback)

	rospy.spin()
