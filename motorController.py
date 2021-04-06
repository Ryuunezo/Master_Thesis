import RPi.GPIO as GPIO

# DC motor controller for Raspberry PI.

class MotorCotroller:
    channel1 = None
    channel2 = None
    channelPWM = None

    # initialization of pins that is use to control motor
    def __init__(self, channel1, channel2, channelPWM=None):
        self.channel1 = channel1
        self.channel2 = channel2
        self.channelPWM = channelPWM
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel1, GPIO.OUT)
        GPIO.setup(self.channel2, GPIO.OUT)
        GPIO.output(self.channel1, GPIO.LOW)
        GPIO.output(self.channel2, GPIO.LOW)
        if channelPWM is not None:  # If channelPWM is None then you can't controll speed, only direction of motor.
            GPIO.setup(self.channelPWM, GPIO.OUT)

    # initialization of pwm, which enable  motor speed control.
    def initPWMcontroll(self, frequency=100, dc=100):
        self.pwm = GPIO.PWM(self.channelPWM, frequency)
        self.pwm.start(dc)

    # motor direction control
    def forward(self):
        GPIO.output(self.channel1, True)
        GPIO.output(self.channel2, False)

    def backward(self):
        GPIO.output(self.channel1, False)
        GPIO.output(self.channel2, True)

    def stop(self):
        GPIO.output(self.channel1, False)
        GPIO.output(self.channel2, False)

    # motor speed control
    def speedChange(self, dc):
        self.pwm.ChangeDutyCycle(dc)

    # clean GPIO pins
    def end(self):
        GPIO.cleanup()
