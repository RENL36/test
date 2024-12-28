from model.units.unit import Unit
from model.resources.food import Food
from model.resources.gold import Gold
from model.resources.wood import Wood


class Archer(Unit):
    """This class represents the Archer unit on the map, inheriting from Unit"""
    def __init__(self):
        super().__init__("Archer", "a", 30, 4, 1.0, { Food: 50 }, 35)
        super().set_range(4)
    
        
