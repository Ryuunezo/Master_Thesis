import pygame
from pygame.locals import *

class SixaxisController:

    def __init__(self, n):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(n)
        self.joystick.init()

    def joystickExit():
        pygame.quit()

    def BUTTON_SELECT(self):
        return self.joystick.get_button(0)

    def BUTTON_L3(self):
        return self.joystick.get_button(1)

    def BUTTON_R3(self):
        return self.joystick.get_button(2)

    def BUTTON_START(self):
        return self.joystick.get_button(3)

    def BUTTON_D_UP(self):
        return self.joystick.get_button(4)

    def BUTTON_D_RIGHT(self):
        return self.joystick.get_button(5)

    def BUTTON_D_DOWN(self):
        return self.joystick.get_button(6)

    def BUTTON_D_LEFT(self):
        return self.joystick.get_button(7)

    def BUTTON_L2(self):
        return self.joystick.get_button(8)

    def BUTTON_R2(self):
        return self.joystick.get_button(9)

    def BUTTON_L1(self):
        return self.joystick.get_button(10)

    def BUTTON_R1(self):
        return self.joystick.get_button(11)

    def BUTTON_TRIANGLE(self):
        return self.joystick.get_button(12)

    def BUTTON_CIRCLE(self):
        return self.joystick.get_button(13)

    def BUTTON_CROSS(self):
        return self.joystick.get_button(14)

    def BUTTON_SQUARE(self):
        return self.joystick.get_button(15)

    def BUTTON_PS(self):
        return self.joystick.get_button(16)

    def HORIZONTAL_LEFT_STICK(self):
        return self.joystick.get_axis(0)

    def VERTICAL_LEFT_STICK(self):
        return self.joystick.get_axis(1)

    def HORIZONTAL_RIGHT_STICK(self):
        return self.joystick.get_axis(2)

    def VERTICAL_RIGHT_STICK(self):
        return self.joystick.get_axis(3)
