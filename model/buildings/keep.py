from model.buildings.building import Building
from model.maps.coordinate import Coordinate

class Keep(Building):
    def __init__(self, position: Coordinate):
        super().__init__(
            name="Keep",
            symbol="K",
            cost={"wood": 35, "gold": 125},
            size=(1, 1),
            health=800,
            max_health=800,
            position=position
        )
        self.attack = 5
        self.range = 8

    def fire_arrow(self, target_position):
        print(f"Keep tire une flèche sur {target_position} avec {self.attack} de dégâts.")