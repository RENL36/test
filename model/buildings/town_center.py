from model.buildings.building import Building
from model.resources.wood import Wood

class TownCenter(Building):
    def __init__(self) -> None:
        super().__init__("Town Center", "T", 1000, {Wood: 100}, 4, 10)
        self.__capacity_increase = 5
        super().set_population_increase(True)
        super().set_resources_drop_point(True)


    def get_capacity_increase(self) -> int:
        """Returns the population capacity of the town center"""
        return self.__capacity_increase
