#!/usr/bin/env python3
import rospy

from str_common_msgs.msg import BoolArray
from std_msgs.msg import UInt16MultiArray

PRODUCT_CODE = "byte CATcode identifier"
DEVICE_SN = "byte Device serial number identifier"

class IOStateNode(object):
    def __init__(self, device_SN):
        rospy.loginfo("this is a test script")
        self.digital_command_publisher = rospy.Publisher("/device_" + PRODUCT_CODE + "_" + device_SN + "_digital_outputs_command", BoolArray, queue_size=, latch=True)
        self.digital_state_subscriber_ = rospy.Subscriber("/device_" + PRODUCT_CODE, + "_" + device_SN, + "_digital_inputs_state", BoolArray, self.digital_state_callback)

    def digital_state_callback(self, msg):
        rospy.loginfo("Recieve data from digital input 0: %f", msg.data[0])

    def test(self):

        output_values = [False, True, False, False, False, False, False, False]
        command_msg = BoolArray(output_values)
        self.digital_command_publisher.publish(command_msg)

        rospy.spin()


if __name__ == "__main__":
    try:
        io_test = IOStateNode(DEVICE_SN)
        io_test.test()
    except rospy.ROSInterruptException:
        sys.stdout.close()
        os.system('clear')
        raise
