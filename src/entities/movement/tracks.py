import time
import math

from entities.movement.limb.limb import Limb
from entities.movement.limb.joints.dcmotor import DCMotor


class Tracks(object):
    """
    Base class for tracks that implements DC motors
    """

    def __init__(self):
        track1pin = 18
        track2pin = 13

        self.track_left = DCMotor(track1pin)
        self.track_right = DCMotor(track2pin)

        print("Tracks setup")

    def move_helper(self, duty_cycle_track_left, duty_cycle_track_right, delay, acceleration, track1direction,
                    track2direction):
        if acceleration <= 0:
            print("Warning, setting acceleration to 0.01")
            acceleration = 0.01

        diff_1 = duty_cycle_track_left - self.track_left.current_speed
        diff_2 = duty_cycle_track_right - self.track_right.current_speed

        step_1 = diff_1 / acceleration / 100
        step_2 = diff_2 / acceleration / 100

        speed_1 = self.track_left.current_speed
        speed_2 = self.track_right.current_speed

        for i in range(0, 100 * acceleration):
            speed_1 += step_1
            speed_2 += step_2

            speed_1 = round(speed_1, 3)
            speed_2 = round(speed_2, 3)

            if speed_1 < 0:
                speed_1 = 0
            if speed_2 < 0:
                speed_2 = 0

            # track direction 1 is forwards, direction 0 is backwards
            if track1direction == 1 and track2direction == 1:
                self.track_left.forward(speed_1, 0)
                self.track_right.forward(speed_2, 0)

            if track1direction == 0 and track2direction == 0:
                self.track_left.backward(speed_1, 0)
                self.track_right.backward(speed_2, 0)

            if track1direction == 1 and track2direction == 0:
                self.track_left.forward(speed_1, 0)
                self.track_right.backward(speed_2, 0)

            if track1direction == 0 and track2direction == 1:
                self.track_left.backward(speed_1, 0)
                self.track_right.forward(speed_2, 0)

            time.sleep(0.01)

        time.sleep(delay)

    def forward(self, duty_cycle, delay, acceleration):
        self.move_helper(duty_cycle, duty_cycle, delay, acceleration, 1, 1)

    def backward(self, duty_cycle, delay, acceleration):
        self.move_helper(duty_cycle, duty_cycle, delay, acceleration, 0, 0)

    def turn_right(self, duty_cycle_track_left, duty_cycle_track_right, delay, acceleration):
        self.move_helper(duty_cycle_track_left, duty_cycle_track_right, delay, acceleration, 1, 0)

    def turn_left(self, duty_cycle_track_right, duty_cycle_track_left, delay, acceleration):
        self.move_helper(duty_cycle_track_left, duty_cycle_track_right, delay, acceleration, 0, 1)
