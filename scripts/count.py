#!/usr/bin/env python3
#SPDX-FileCopyrightText:2022 Ryuich Ueda + Takeru Matsumoto
#SPDX-License-Identifier:BSD-3-Clause License
import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(2)
n = 0
while not rospy.is_shutdown():
    n += 1
    pub.publish(n)
    rate.sleep()
