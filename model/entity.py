from model.game_object import GameObject
from model.resources.resource import Resource

class Entity(GameObject):
    """This class represents the entities(Units and Buildings) on the map"""
    def __init__(self, name: str, letter: str, hp: int, cost: dict[Resource, int], spawning_time: int):
        super().__init__(name, letter, hp, cost, spawning_time)
        self.__cost: dict[Resource, int] = cost
        self.__spawning_time: int = spawning_time
    
    def get_cost(self) -> dict[Resource, int]:
        return self.__cost
    
    def get_spawning_time(self) -> int:
        return self.__spawning_time