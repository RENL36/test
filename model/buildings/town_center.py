from model.buildings.building import Building
from model.resources import Wood

class TownCenter(Building):
    def __init__(self) -> None:
        super().__init__("Town Center", "T", 1000, {Wood: 100}, 4, 10)
        self.__population = 0
        self.__capacity = 5

    def get_population(self) -> int:
        """Returns the population of the town center"""
        return self.__population

    def get_capacity(self) -> int:
        """Returns the population capacity of the town center"""
        return self.__capacity
    
    def add_capacity(self, amount: int) -> None:
        """Adds to the population capacity of the town center"""
        if amount < 1:
            raise ValueError("Amount must be greater than 0")
        if self.get_population() + amount > self.get_capacity():
            raise ValueError("Population exceeds capacity")
        self.__capacity += amount

    def remove_capacity(self, amount: int) -> None:
        """Removes from the population capacity of the town center"""
        if amount < 1:
            raise ValueError("Amount must be greater than 0")
        if self.get_population() - amount < 0:
            raise ValueError("Population cannot be negative")
        self.__capacity -= amount