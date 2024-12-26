from model.game_object import GameObject
import typing
if typing.TYPE_CHECKING:
    from model.resources.resource import Resource

class Entity(GameObject):
    """This class represents the entities (Units and Buildings) on the map."""
    
    def __init__(self, name: str, letter: str, hp: int, cost: dict['Resource', int], spawning_time: int):
        """
        Initializes the entity.

        :param name: The name of the entity.
        :type name: str
        :param letter: The letter representing the entity.
        :type letter: str
        :param hp: The hit points of the entity.
        :type hp: int
        :param cost: The cost of the entity in resources.
        :type cost: dict['Resource', int]
        :param spawning_time: The time it takes to spawn the entity.
        :type spawning_time: int
        """
        super().__init__(name, letter, hp)
        self.__cost: dict['Resource', int] = cost
        self.__spawning_time: int = spawning_time
    
    def get_cost(self) -> dict['Resource', int]:
        """
        Returns the cost of the entity.

        :return: The cost of the entity in resources.
        :rtype: dict['Resource', int]
        """
        return self.__cost
    
    def get_spawning_time(self) -> int:
        """
        Returns the spawning time of the entity.

        :return: The spawning time of the entity.
        :rtype: int
        """
        return self.__spawning_time