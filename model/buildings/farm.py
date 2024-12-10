from model.buildings.building import Building
from model.maps.coordinate import Coordinate

class Farm(Building):
    def __init__(self, position: Coordinate):
        super().__init__(
            name="Farm",
            symbol="F",
            cost={"wood": 60},
            size=(2, 2),
            health=100,
            max_health=100,
            position=position,
            image_path=""" image associé """
        )
        self.food_capacity = 300  # Contient 300 unités de nourriture