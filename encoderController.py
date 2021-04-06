import RPi.GPIO as gpio
from time import sleep


class EncoderController:

    def __init__(self, diode, irSensor):
        self.diode = diode
        self.irSensor = irSensor
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)
        gpio.setup(self.diode, gpio.OUT, initial=gpio.LOW)
        gpio.setup(self.irSensor, gpio.IN)

    def encoderOn(self):
        gpio.output(self.diode, gpio.HIGH)

    def encoderOff(self):
        gpio.output(self.diode, gpio.LOW)

    def encoderState(self, time=0):
        sleep(time)
        return gpio.input(self.irSensor)

    def updatePreviousState(self, lastState, currentState):
        self.lastState = currentState
        return lastState

    def encoderStep(self, turn, value):
        return value + turn

    def encoderSet(self, value):
        return value

    def encoderReset(self):
        return 0
