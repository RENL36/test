from model.units.unit import Unit
from model.resources import *
from util.coordinate import Coordinate
import typing
if typing.TYPE_CHECKING:
    from util.map import Map

class Archer(Unit):
    """This class represents the Archer unit on the map, inheriting from Unit"""
    def __init__(self):
        super().__init__("Archer", "a", 30, 4, 1.0, { Food: 50 }, 35)
        self.__range: int = 4
    
    def get_range(self):
        return self.__range
        
