from model.entity import Entity
import typing
if typing.TYPE_CHECKING:
    from model.resources.resource import Resource
class Building(Entity):
    def __init__(self, name: str, letter: str, hp: int, cost: dict['Resource', int], size: int, spawning_time: int):
        """Initializes the building"""
        self.__resources_drop_point: bool = False
        self.__population_increase: bool = False
        super().__init__(name, letter, hp, cost, spawning_time)
        super().set_size(size)
        super().set_sprite_path(f"assets/sprites/buildings/{self.get_name().lower}.png")

    def is_resources_drop_point(self) -> bool:
        """Returns whether or not the building is a resources drop point"""
        return self.__resources_drop_point
    
    def set_resources_drop_point(self, resources_drop_point: bool) -> None:
        """Sets whether or not the building is a resources drop point"""
        self.__resources_drop_point = resources_drop_point
    
    def is_population_increase(self) -> bool:
        """Returns whether or not the building increases the population"""
        return self.__population_increase
    
    def set_population_increase(self, population_increase: bool) -> None:
        """Sets whether or not the building increases the population"""
        self.__population_increase = population_increase
    