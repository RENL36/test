from model.buildings.building import Building
from model.maps.coordinate import Coordinate

class TownCenter(Building):
    def __init__(self, position: Coordinate):
        super().__init__(
            name="Town Center",
            symbol="T",
            cost={"wood": 350},
            size=(4, 4),
            health=1000,
            max_health=1000,
            position=position
        )
        self.population_capacity = 5

    def spawn_villager(self):
        print(f"Villageois créé depuis {self.name} à {self.position}")