from model.units.unit import Unit
from model.resources.food import Food
from model.resources.gold import Gold
from model.resources.wood import Wood

class Horseman(Unit):
    """This class represents the Horseman the map, inheriting from Unit"""
    def __init__(self):
        super().__init__("Horseman", "h", 45, { Food : 50, Gold: 20},30, 4,  1.2)

    
        