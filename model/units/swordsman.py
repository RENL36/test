from model.units.unit import Unit
from model.resources import *
from util.coordinate import Coordinate
import typing
if typing.TYPE_CHECKING:
    from util.map import Map


class Swordsman(Unit):
    """This class represents the Swordsman unit on the map, inheriting from Unit"""
    def __init__(self):
        super().__init__("Swordsman", "s", 40, 4, 0.9, { Food: 50, Gold: 20 }, 20)

    
        