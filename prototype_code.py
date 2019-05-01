#!/usr/bin/env python3
import ev3dev.ev3
import random
import time

motor_left = ev3.LargeMotor('outB') 
motor_right = ev3.LargeMotor('outC') 
u_sensor = ev3.UltrasonicSensor('in4') 
c_sensor = ev3.ColorSensor('in3') 
g_sensor = ev3.GyroSensor('in2') 
# Ultrasonic sensor setup
u_sensor.mode='US-DIST-CM'
units = u_sensor.units 
distance = u_sensor.value()/10 
# Gyro setup
g_sensor.mode='GYRO-ANG'
# Color sensor Setup
c_sensor.mode='COL-COLOR'

#========================================================================================= 
def moveForward():
    motor_left.run_direct(duty_cycle_sp=75) 
    motor_right.run_direct(duty_cycle_sp=75)
    # move for 2 seconds
    # TODO: change this to make sure it moves one space
    # TODO: come up with a better method for moving 1 space accurately
    time.sleep(2)
    stopMotors()
        
#========================================================================================= 
def turnRight(): 
    motor_left.run_direct(duty_cycle_sp=75) 
    motor_right.run_direct(duty_cycle_sp=-75)

#=========================================================================================
def stopMotors():
    motor_left.stop(stop_action="brake")
    motor_right.stop(stop_action="brake")
    
#=========================================================================================
def canMoveForward():
    # TODO: tweak this value to make sure it works 
    return distance <= 5
        
#=========================================================================================
def isAtFinish():
    return c_sensor.value() == 1

#=========================================================================================

def turnUntil(deg):
    turnRight()

    while g_sensor.value() < deg:
        time.sleep(0.001)
    
    stopMotors()

def randomTurn():
    turnOptions = [90, 180, 270]
    randomDeg = turnOptions[random.randint(0,len(turnOptions) - 1)]
    turnUntil(randomDeg)

def mainLoop():
    if isAtFinish():
        # check if we're at the finish and end the program if needed
        return True
    
    randomTurn()
    if canMoveForward():
        moveForward()
    return False

# Run mainLoop until it returns True
while mainLoop() != True:
  pass
