from model.buildings.building import Building
from model.maps.coordinate import Coordinate

class House(Building):
    def __init__(self, position: Coordinate):
        super().__init__(
            name="House",
            symbol="H",
            cost={"wood": 25},
            size=(2, 2),
            health=200,
            max_health=200,
            position=position
        )
        self.population_capacity = 5