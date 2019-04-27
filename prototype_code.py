#!/usr/bin/env python3
#import ev3dev.ev3
import sys

sys.stdout.write("code")

def LogEvent(evtName, msg):
    sys.stdout.write("Event: " + evtName + " - Msg: " + msg + "\n")

def FakeTurnLeft(args): 
    LogEvent("LeftMotor", args["duty_cycle_sp"])

def FakeTurnRight(args): 
    LogEvent("RightMotor", args["duty_cycle_sp"])

if ev3 
    motor_left = ev3.LargeMotor('outB') 
    motor_right = ev3.LargeMotor('outC') 
    u_sensor = ev3.UltrasonicSensor('in4') 
    c_sensor = ev3.ColorSensor('in3') 
    g_sensor = ev3.GyroSensor('in2') 
else
    motor_left = {
        "run_direct": FakeTurnLeft  
    }
    motor_right = {
        "run_direct": FakeTurnRight
    }
    u_sensor = None
    c_sensor = None

#========================================================================================= 
def MoveForward(): 

   motor_left.run_direct(duty_cycle_sp=75) 
   motor_right.run_direct(duty_cycle_sp=75)
#========================================================================================= 
def MoveBackward(): 

   motor_left.run_direct(duty_cycle_sp=-75) 
   motor_right.run_direct(duty_cycle_sp=-75) 
#========================================================================================= 
def TurnLeft(): 

   motor_left.run_direct(duty_cycle_sp=-75) 
   motor_right.run_direct(duty_cycle_sp=75) 
#========================================================================================= 
def TurnRight(): 

   motor_left.run_direct(duty_cycle_sp=75) 
   motor_right.run_direct(duty_cycle_sp=-75)
#=========================================================================================

def StopMotors()
    motor_left.run_direct(duty_cycle_sp=0)
    motor_right.run_direct(duty_cycle_sp=0)

isDriving = False

def drive():
    # check if we can still move forward
    if canMoveForward()
        isDriving = True
        MoveForward()
    else
        isDriving = False
        StopMotors()

def turnUntil(deg):
    TurnRight()

    while gyro.value < deg
        sleep(0.001)

def randomTurn():
    turnOptions = [90, 180, 270]
    randomDeg = turnOptions[random.randint(0,len(turnOptions) - 1)]
    turnUntil(randomDeg)

def mainLoop()
    if isAtFinish()
        # check if we're at the finish and end the program if needed
        return True
    else if canMoveForward()
        # move us forward
        moveForward()
    else
        randomTurn()
    return False

while !mainLoop()

