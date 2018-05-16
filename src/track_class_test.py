from entities.movement.limb.tracks import Tracks

tracks = Tracks()

for cycle in range(0, 20):
    tracks.forward(cycle, 0.5)

for cycle in range(0, 20):
    tracks.backward(cycle, 0.5)

for cycle in range(0, 20):
    tracks.turn_right(cycle, cycle, 0.5)

for cycle in range(0, 20):
    tracks.turn_left(cycle, cycle, 0.5)
