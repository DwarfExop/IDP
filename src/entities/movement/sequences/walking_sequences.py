import sys

sys.path.insert(0, '../../../../src')

from entities.movement.sequences.sequences import *


def walk_forward(legs, speeds, self_update=True, sequences=None):
    if sequences is None:
        sequences = [0, 1, 2, 3]

    for moves in sequences:
        legs.move(leg_0_moves=forward_sequence[moves][0],
                  leg_1_moves=forward_sequence[moves][1],
                  leg_2_moves=forward_sequence[moves][2],
                  leg_3_moves=forward_sequence[moves][3],
                  delay=0,
                  speeds=speeds,
                  self_update=self_update)


def walk_forward_repeat(legs, speeds, repeat):
    for i in range(repeat):
        walk_forward(legs, speeds)


def walk_backward(legs, speeds, self_update=True, sequences=None):
    if sequences is None:
        sequences = [0, 1, 2, 3]

    for moves in sequences:
        legs.move(leg_0_moves=backward_sequence[moves][0],
                  leg_1_moves=backward_sequence[moves][1],
                  leg_2_moves=backward_sequence[moves][2],
                  leg_3_moves=backward_sequence[moves][3],
                  delay=0,
                  speeds=speeds,
                  self_update=self_update)


def walk_backward_repeat(legs, speeds, repeat):
    for i in range(repeat):
        walk_backward(legs, speeds)


def enge_dab(legs, speeds):
    print("ENGE DAB")
    legs.move(leg_0_moves=[315, 678, 1023],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0.1,
              speeds=speeds)


def wave(legs, speeds, repeat):
    for i in range(repeat):
        legs.move(leg_0_moves=[527, 680, 998],
                  leg_1_moves=[650, 400, 400],
                  leg_2_moves=[400, 400, 400],
                  leg_3_moves=[600, 400, 400],
                  delay=0.1,
                  speeds=speeds)
        legs.move(leg_0_moves=[527, 750, 900],
                  leg_1_moves=[650, 400, 400],
                  leg_2_moves=[400, 400, 400],
                  leg_3_moves=[600, 400, 400],
                  delay=0.1,
                  speeds=speeds)


def lol(legs, speeds, repeat):
    for i in range(repeat):
        legs.move(leg_0_moves=[315, 678, 1023],
                  leg_1_moves=[650, 400, 400],
                  leg_2_moves=[400, 400, 400],
                  leg_3_moves=[600, 400, 400],
                  delay=0.1,
                  speeds=speeds)
        legs.move(leg_0_moves=[729, 821, 966],
                  leg_1_moves=[650, 400, 400],
                  leg_2_moves=[400, 400, 400],
                  leg_3_moves=[600, 400, 400],
                  delay=0.1,
                  speeds=speeds)


def pull(legs, speeds):
    legs.move(leg_0_moves=[530, 730, 640],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)
    legs.move(leg_0_moves=[530, 650, 640],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)
    legs.move(leg_0_moves=[530, 650, 750],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)
    legs.move(leg_0_moves=[530, 840, 970],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)


def push(legs, speeds):
    legs.move(leg_0_moves=[530, 650, 750],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)
    legs.move(leg_0_moves=[530, 650, 640],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)
    legs.move(leg_0_moves=[530, 730, 640],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)
    legs.move(leg_0_moves=[530, 840, 970],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)


def march(legs, speeds):
    legs.move(leg_0_moves=[530, 600, 570],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)
    legs.move(leg_0_moves=[530, 730, 690],
              leg_1_moves=[650, 400, 400],
              leg_2_moves=[400, 400, 400],
              leg_3_moves=[600, 400, 400],
              delay=0,
              speeds=speeds)

