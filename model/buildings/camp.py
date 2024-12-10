from model.buildings.building import Building
from model.maps.coordinate import Coordinate

class Camp(Building):
    def __init__(self, position: Coordinate):
        super().__init__(
            name="Camp",
            symbol="C",
            cost={"wood": 100},
            size=(2, 2),
            health=200,
            max_health=200,
            position=position,
            image_path=""" image associé"""
        )

    def drop_resources(self, resource_type, amount):
        print(f"{amount} de {resource_type} déposés au {self.name}.")