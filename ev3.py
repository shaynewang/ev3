#!/usr/bin/env python3
from ev3dev import ev3 
import time

#Setting up motors 
turning_wheel = ev3.MediumMotor('outA')
rear_l        = ev3.LargeMotor('outB')
rear_r        = ev3.LargeMotor('outC')

#Setting up sensors
IR_sensor     = ev3.InfraredSensor()
assert IR_sensor.connected
#distance mode
IR_sensor.mode='IR-PROX'

run_time = 1000000
time_to_turn = 1
turn = 100

rear_l.run_timed(time_sp=run_time,speed_sp=-500)
rear_r.run_timed(time_sp=run_time,speed_sp=-500)
print("going!")
print(rear_l.state)
startdistance = IR_sensor.value()
print("IR sensor output: ",startdistance)
start_time = time.time()
while rear_l.state and rear_r.state:
	distance = IR_sensor.value()
	print("IR sensor output: ",distance)
	if distance < 60:
	    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
	    if distance < 30:
	        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
	        turning_wheel.stop()
	        rear_l.stop()
	        rear_r.stop()
	        break
	else:
     	    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
	turning_wheel.run_to_rel_pos(position_sp = turn, speed_sp = 1000)
	if time.time() - start_time > time_to_turn:
		turn = -turn
		start_time = time.time()

ev3.Sound.beep()       
ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN) 
ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN) 
print("done!")
