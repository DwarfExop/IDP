#!/bin/python

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

class DCMotor(object):
    """
    Base class for dc motor
    """

    def __init__(self, frequency):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.pinMotorForward = 10
        self.pinMotorBackward = 9
        self.pinPwm = 18
        self.frequency = frequency
        self.stop = 0
        GPIO.setup(self.pinPwm, GPIO.OUT)
        GPIO.setup(self.pinMotorForward, GPIO.OUT)
        GPIO.setup(self.pinMotorBackward, GPIO.OUT)
        self.pwmMotor = GPIO.PWM(self.pinPwm, self.frequency)
        self.pwmMotor.start(self.stop)

    # Turn all motors off
    def stopMotor(self):
        self.pwmMotor.ChangeDutyCycle(self.stop)

    # Turn both motors forwards
    def forward(self, dutycycle):
        print("Forwards " + str(dutycycle))
        GPIO.output(self.pinMotorForward, GPIO.HIGH)
        GPIO.output(self.pinMotorBackward, GPIO.LOW)
        self.pwmMotor.ChangeDutyCycle(dutycycle)

    def backward(self, dutycycle):
        print("Backwards " + str(dutycycle))
        GPIO.output(self.pinMotorForward, GPIO.LOW)
        GPIO.output(self.pinMotorBackward, GPIO.HIGH)
        self.pwmMotor.ChangeDutyCycle(dutycycle)


def main():
    dvigatel = DCMotor(20)
    dvigatel.forward(20)

main()
