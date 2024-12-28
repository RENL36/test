from model.entity import Entity
import typing
if typing.TYPE_CHECKING:
    from model.resources.resource import Resource

class Unit(Entity):
    """This class represents the units on the map."""

    def __init__(self, name: str, letter: str, hp: int, cost: dict['Resource', int], spawning_time: int, attack_per_second: int, speed: float):
        """
        Initializes the unit.

        :param name: The name of the unit.
        :type name: str
        :param letter: The letter representing the unit.
        :type letter: str
        :param hp: The hit points of the unit.
        :type hp: int
        :param cost: The cost to create the unit.
        :type cost: dict['Resource', int]
        :param spawning_time: The time it takes to spawn the unit.
        :type spawning_time: int
        :param attack_per_second: The attack rate of the unit.
        :type attack_per_second: int
        :param speed: The speed of the unit.
        :type speed: float
        """
        super().__init__(name, letter, hp, cost, spawning_time)
        self.__attack_per_second: int = attack_per_second
        self.__speed: float = speed
        super().set_sprite_path(f"assets/sprites/units/{self.get_name().lower()}.png")

    def get_attack_per_second(self) -> int:
        """
        Returns the attack rate of the unit.

        :return: The attack rate of the unit.
        :rtype: int
        """
        return self.__attack_per_second
    
    def get_speed(self) -> float:
        """
        Returns the speed of the unit.

        :return: The speed of the unit.
        :rtype: float
        """
        return self.__speed