from model.units.unit import Unit
from model.resources.food import Food
from model.resources.resource import Resource

class Villager(Unit):
    """This class represents the Villager unit"""

    def __init__(self):
        """Initializes the villager"""
        super().__init__("Villager", "V", 25, {Food: 50}, 25, 2, 0.8)        
        self.inventory: dict[Resource, int] = {}
        self.inventory_size: int = 20
        self.collect_time_per_minute: int = 25