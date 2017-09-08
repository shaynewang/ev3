#!/usr/bin/env python3
from ev3dev import ev3 
import time

turning_wheel = ev3.MediumMotor('outA')
rear_l = ev3.LargeMotor('outB')
rear_r = ev3.LargeMotor('outC')

run_time = 10000

rear_l.run_timed(time_sp=run_time,speed_sp=-500)
rear_r.run_timed(time_sp=run_time,speed_sp=-500)
print("going!")
print(rear_l.state)
turn = 100
for i in range(20):
	turning_wheel.run_to_rel_pos(position_sp = turn, speed_sp = 1000)
	time.sleep(0.5)
	turn = -turn
