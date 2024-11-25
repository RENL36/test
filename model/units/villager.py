from model.units.unit import Unit
from model.resources.resource import Resource

class Villager(Unit):
    def __init__(self):
        super().__init__("Villager", "V", 25, 2, 0.8, { "F": 50 }, 25)
        self.inventory: dict[Resource, int] = {}
        self.inventory_size: int = 20
        self.collect_time_per_minute: int = 25