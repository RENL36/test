from model.units.unit import Unit
from model.resources import *
from util.coordinate import Coordinate
import typing
if typing.TYPE_CHECKING:
    from util.map import Map

class Horseman(Unit):
    """This class represents the Horseman the map, inheriting from Unit"""
    def __init__(self):
        super().__init__("Horseman", "h", 45, 4, 1.2, { Food : 50, Gold: 20}, 30)

    
        