"""
This file contains the Coordinate class which is used to represent the coordinates of the tiles in the grid and the methods associated with it.
"""
class Coordinate:
    """Used to represent the coordinates of the tiles in the grid."""
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
    
    def set_x(self, x: int) -> None:
        """Setter method for the x coordinate"""
        self.__x = x
    
    def set_y(self, y: int) -> None:
        """Setter method for the y coordinate"""
        self.__y = y
    
    def get_x(self) -> int:
        """Getter method for the x coordinate"""
        return self.__x
    
    def get_y(self) -> int:
        """Getter method for the y coordinate"""
        return self.__y
    
    def distance(self, other: 'Coordinate') -> int:
        """Distance method is used to calculate the number of steps between two tiles"""
        if not isinstance(other, Coordinate):
            return None
        return abs(self.get_x() - other.get_x()) + abs(self.get_y() - other.get_y())
    
    def is_in_range(self, other: 'Coordinate', distance_range: int) -> bool:
        """Method to check if the distance between two tiles is less than or equal to a certain range (almost equal included)"""
        if not isinstance(other, Coordinate):
            return False
        return self.distance(other) <= distance_range
    
    def __hash__(self) -> int:
        """Hash for the coordinates to be read by the dictionary"""
        return hash((self.__x, self.__y))
    
    def __eq__(self, other) -> bool:
        """Equality check for the coordinates"""
        if not isinstance(other, Coordinate):
            return False
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()
    
    def __str__(self) -> str:
        """String representation of the coordinates"""
        return f"({self.get_x()},{self.get_y()})"