#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
import RPi.GPIO as GPIO

GPIO_PIN = 16

if __name__ == '__main__':
	rospy.init_node('pin_state_publisher')
	
	pub = rospy.Publisher('button_state', Bool, queue_size = 10)

	#configuring GPIO pin
	# pull_up_down = GPIO.PUD_UP is push up resistor 
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	
	while not rospy.is_shutdown():
		gpio_state = not GPIO.input(GPIO_PIN)
		rospy.loginfo(gpio_state)
		rate.sleep()

	#upon exiting program will clean up all pins used
	GPIO.cleanup()
