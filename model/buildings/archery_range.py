from model.buildings.building import Building
from model.maps.coordinate import Coordinate

class ArcheryRange(Building):
    def __init__(self, position: Coordinate):
        super().__init__(
            name="Archery Range",
            symbol="A",
            cost={"wood": 175},
            size=(3, 3),
            health=500,
            max_health=500,
            position=position
        )

    def spawn_archer(self):
        print(f"Archer créé depuis {self.name} à {self.position}")