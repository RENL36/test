from model.resources.food import Food
from model.resources.gold import Gold
from model.resources.wood import Wood
from model.resources.resource import Resource
from model.units.unit import Unit
from model.buildings.building import Building
from typing import Set

class Player:
    """This class represents the player (AI) in the game."""

    def __init__(self, name: str, color: str) -> None:
        """
        Initializes the player with the given name and color.

        :param name: The name of the player.
        :type name: str
        :param color: The color of the player.
        :type color: str
        """
        self.__name: str = name
        self.__color: str = color
        self.__resource: dict[Resource, int] = {Food: 0, Gold: 0, Wood: 0}
        self.__units: Set[Unit] = set()
        self.__unit_count: int = 0
        self.__buildings: Set[Building] = set()
        self.__max_population: int = 0
    
    def get_name(self) -> str:
        """
        Returns the name of the player.

        :return: The name of the player.
        :rtype: str
        """
        return self.__name
    
    def get_color(self) -> str:
        """
        Returns the color of the player.

        :return: The color of the player.
        :rtype: str
        """
        return self.__color
    
    def get_resources(self) -> dict[Resource, int]:
        """
        Returns the resources of the player.

        :return: A dictionary of resources and their amounts.
        :rtype: dict[Resource, int]
        """
        return self.__resource

    def collect(self, resource: Resource, amount: int) -> None:
        """
        Adds a resource to the player.

        :param resource: The type of resource to add.
        :type resource: Resource
        :param amount: The amount of the resource to add.
        :type amount: int
        """
        if resource in self.__resource:
            self.__resource[resource] += amount
        
    def check_consume(self, resource: Resource, amount: int) -> bool:
        """
        Checks if the player has enough resources to consume.

        :param resource: The type of resource to check.
        :type resource: Resource
        :param amount: The amount of the resource to check.
        :type amount: int
        :return: True if the player has enough resources, False otherwise.
        :rtype: bool
        """
        return self.__resource[resource] >= amount

    def consume(self, resource: Resource, amount: int) -> None:
        """
        Uses a resource from the player.

        :param resource: The type of resource to consume.
        :type resource: Resource
        :param amount: The amount of the resource to consume.
        :type amount: int
        :raises ValueError: If there are not enough resources to consume.
        """
        if not self.check_consume(resource, amount):
            raise ValueError("Not enough resources to consume")
        self.__resource[resource] -= amount
    
    def get_units(self) -> Set[Unit]:
        """
        Returns the units of the player.

        :return: A set of units.
        :rtype: Set[Unit]
        """
        return self.__units
    
    def get_unit_count(self) -> int:
        """
        Returns the number of units of the player.

        :return: The number of units.
        :rtype: int
        """
        return self.__unit_count
    
    def add_unit(self, unit: Unit) -> None:
        """
        Adds a unit to the player.

        :param unit: The unit to add.
        :type unit: Unit
        :raises ValueError: If the player has reached the maximum population.
        """
        if not self.__unit_count < self.__max_population:
            raise ValueError("Player has reached the maximum population")
        self.__units.add(unit)
        self.__unit_count += 1

    def remove_unit(self, unit: Unit) -> None:
        """
        Removes a unit from the player.

        :param unit: The unit to remove.
        :type unit: Unit
        """
        self.__units.remove(unit)
        self.__unit_count -= 1

    def get_buildings(self) -> Set[Building]:
        """
        Returns the buildings of the player.

        :return: A set of buildings.
        :rtype: Set[Building]
        """
        return self.__buildings

    def add_building(self, building: Building) -> None:
        """
        Adds a building to the player.

        :param building: The building to add.
        :type building: Building
        """
        self.__buildings.add(building)

    def remove_building(self, building: Building) -> None:
        """
        Removes a building from the player.

        :param building: The building to remove.
        :type building: Building
        """
        self.__buildings.remove(building)
    
    def get_max_population(self) -> int:
        """
        Returns the maximum population of the player.

        :return: The maximum population.
        :rtype: int
        """
        return self.__max_population