from model.buildings.building import Building
from model.maps.coordinate import Coordinate

class Stable(Building):
    def __init__(self, position: Coordinate):
        super().__init__(
            name="Stable",
            symbol="S",
            cost={"wood": 175},
            size=(3, 3),
            health=500,
            max_health=500,
            position=position
        )

    def spawn_horseman(self):
        print(f"Horseman créé depuis {self.name} à {self.position}")