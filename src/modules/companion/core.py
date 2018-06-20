import sys

sys.path.insert(0, '../../../src')

from entities.vision.helpers.json_handler import Json_Handler
from entities.vision.vision import Vision
from entities.vision.helpers.vision_helper import Color
from entities.vision.recognize_settings import Recognize_settings
from entities.threading.utils import SharedObject


def run(name, control):

    print("[RUN] " + str(name))

    shoe = [Color("red", [167, 116, 89], [180, 255, 255])]

    json_handler = Json_Handler(shoe, "shoe_ranges")
    color_range = json_handler.get_color_range()

    vision = Vision(json_handler, SharedObject())

    vision.recognize.run(color_range)