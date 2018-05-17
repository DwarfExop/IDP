from entities.movement.tracks import Tracks


class Movement(object):
    """
    Base class for movement
    """

    def __init__(self, limbs, lights):
        tracks = []
        legs = []
        tire = []
        for limb in limbs:
            if limb.type == 'track':
                tracks.append(limb)
            elif limb.type == 'leg':
                legs.append(limb)
            elif limb.type == 'tire':
                tire.append(limb)

        self.limbs = limbs
        self.lights = lights
        self.tracks = Tracks(tracks)

    def forward(self):
        self.tracks.forward()

    def backward(self):
        self.tracks.backward()

    def turn_left(self):
        self.tracks.turn_left()

    def turn_right(self):
        self.tracks.turn_right()
