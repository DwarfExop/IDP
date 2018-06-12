import sys
import time

sys.path.insert(0, '../../../src')


def run(name, movement, shared_object):
    print("run " + str(name))

    while not shared_object.has_to_stop():
        print("Doing calculations and stuff")

        movement.tracks.turn_right(100, 100, 0, 0)

    # Notify shared object that this thread has been stopped
    print("Stopped" + str(name))
    shared_object.has_been_stopped()
