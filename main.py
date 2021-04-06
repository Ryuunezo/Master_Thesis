'''
The aim of the master's thesis was to develop a concept and to create the universal driver for GOTO system
which can be easily modified by users (the user can modify the software by adding new code / class to the program).
GOTO system is computerized mount for telescope which has electric motors to control it position
and driver which change digital signal from controller to electrical that goes to motors.

As a driver in the project was used Raspberry Pi

'''

from time import sleep
from motorController import MotorCotroller
from encoderController import EncoderController
from sixaxisController import SixaxisController
import time
import pygame

# Define GPIO pins for controlling motors
pinDC1 = 16
pinDC2 = 18
pinDC3 = 29
pinDC4 = 31
pinPWM1 = 22
pinPWM2 = 37

# Define GPIO pins for encoder
pinDiode1 = 11
pinIR1 = 13

# Initialization of two motors with PWM speed control
dc = 100
speed = 0
motor1 = MotorCotroller(pinDC1, pinDC2, pinPWM1)
motor2 = MotorCotroller(pinDC3, pinDC4, pinPWM2)
motor1.initPWMcontroll(400, 10)
motor2.initPWMcontroll(400, 10)

# Initialization of encoder
encoder = EncoderController(pinDiode1, pinIR1)
lastState = encoder.encoderState()
currentState = 0
stepValue = 0
setValue = 0
_startStop = 0
lastTime = 0

# initialization of PlayStation 3  controller
psController = SixaxisController(0)

try:
    while 1:
        
        sleep(0.01)
        events = pygame.event.get()
        
        for event in events:

            # Block of code responsible for controlling first DC motor directions by using controller left joystick.
            # Block also contains code responsible for encoder which can provide information about speed,
            # position and direction of motor
            if psController.VERTICAL_LEFT_STICK() > 0.6:
                newTime = time.time()
                encoder.encoderOn()
                currentState = encoder.encoderState()
                if currentState != lastState:
                    # ct = newTime-lastTime
                    # lastTime = time.time()
                    lastState = encoder.updatePreviousState(lastState, currentState)
                    stepValue = encoder.encoderStep(1, stepValue)
                    # print('EncoderSignal: '+str(stepValue) + '| Time between signal: ' + str(ct))
                motor1.forward()
            elif psController.VERTICAL_LEFT_STICK() < -0.6:
                newTime = time.time()
                encoder.encoderOn()
                currentState = encoder.encoderState()
                if currentState != lastState:
                    # ct = newTime-lastTime
                    # lastTime = time.time()
                    lastState = encoder.updatePreviousState(lastState, currentState)
                    stepValue = encoder.encoderStep(-1, stepValue)
                    # print('EncoderSignal: '+str(stepValue) + '| Time between signal: ' + str(ct))
                motor1.backward()
            elif 0.6 > psController.VERTICAL_LEFT_STICK() > -0.6:
                encoder.encoderOff()
                motor1.stop()

            # Block of code responsible for controlling second DC motor directions by using controller right joystick.
            if psController.HORIZONTAL_RIGHT_STICK() > 0.6:
                motor2.forward()
            elif psController.HORIZONTAL_RIGHT_STICK() < -0.6:
                motor2.backward()
            elif 0.6 > psController.HORIZONTAL_RIGHT_STICK() > -0.6:
                motor2.stop()

            # Changing motor speed. The speed can be change between 0 and 4.
            if psController.BUTTON_R1() == 1:
                if speed < 5:
                    speed += 1
                    motor1.speedChange(speed*15+10)
                    motor2.speedChange(speed*15+10)
            elif psController.BUTTON_L1() == 1:
                if speed > 0:
                    speed -= 1
                    motor1.speedChange(speed*15+10)
                    motor2.speedChange(speed*15+10)

            # Setting new position as a base
            if psController.BUTTON_SELECT() == 1:
                setValue = encoder.encoderSet(stepValue)

            # Resetting encoder position
            if psController.BUTTON_SQUARE() == 1:
                stepValue = encoder.encoderReset()

            # Algorithm which allow user to move motors to previous save position.
            if psController.BUTTON_START() == 1:
                
                _diffSteps = setValue - stepValue

                while _diffSteps != 0:
                    newTime = time.time()
                    encoder.encoderOn()
                    currentState = encoder.encoderState()

                    if _diffSteps > 0:
                        if currentState != lastState:
                            # ct = newTime-lastTime
                            # lastTime = time.time()
                            lastState = encoder.updatePreviousState(lastState, currentState)
                            _diffSteps = encoder.encoderStep(-1, _diffSteps)
                            # print('EncoderSignal: '+str(_diffSteps) + '| Time between signal: ' + str(ct))
                        motor1.backward()
                    elif _diffSteps < 0:
                        if currentState != lastState:
                            # ct = newTime-lastTime
                            # lastTime = time.time()
                            lastState = encoder.updatePreviousState(lastState, currentState)
                            _diffSteps = encoder.encoderStep(1, _diffSteps)
                            # print('EncoderSignal: '+str(_diffSteps) + '| Time between signal: ' + str(ct))
                            # print(_diffSteps)
                        motor1.forward()

# Idea for algorithm which should allows users to fallow object.
# The position of object is captured by camera (

            # if psController.BUTTON_TRIANGLE() == 1:
            #     x0 = stepValue
            #     centerX = x0
            #     rangeX = 10
            #     n = 0
            #     speed = 10
            #
            #     while psController.BUTTON_CIRCLE() == 0:
            #         encoder.encoderOn()
            #         currentState = encoder.encoderState()
            #         if n == 1000:
            #             x0 -= random.rand()*100
            #         else:
            #             x0 += random.rand()
            #
            #         newcenterX = centerX
            #
            #         if x0 > centerX:
            #             speed = (x0-centerX)/rangeX
            #             if 10+speed*100 > 100:
            #                 motor1.speedChange(100)
            #             else:
            #                 motor1.speedChange(10+speed*100)
            #             if currentState != lastState:
            #                 lastState = encoder.updatePreviousState(lastState, currentState)
            #                 newcenterX = encoder.encoderStep(1, newcenterX)
            #                 print(stepValue)
            #             motor1.forward()
            #
            #         if x0 < centerX:
            #             speed = (x0-centerX)/rangeX
            #             if 10+abs(newcenterX)*100 > 100:
            #                 motor1.speedChange(0)
            #             else:
            #                 motor1.speedChange(10+speed*10)
            #             if currentState != lastState:
            #                 lastState = encoder.updatePreviousState(lastState, currentState)
            #                 newcenterX = encoder.encoderStep(-1, newcenterX)
            #             motor1.backward()
            #
            #         centerX = newcenterX
            #         n += 1
                            
except KeyboardInterrupt:
    psController.joystickExit()
    motor1.end()
    motor2.end()
