"""
This file contains the Coordinate class which is used to represent the coordinates of the tiles in the grid and the methods associated with it.
"""
class Coordinate:
    def __init__(self, x: int, y: int):
        """Used to represent the coordinates of the tiles in the grid."""
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

    def __hash__(self) -> int:
        """Hash for the coordinates to be read by the dictionary"""
        return hash((self.__x, self.__y))
    
    def __eq__(self, other) -> bool:
        """Equality check for the coordinates"""
        if not isinstance(other, Coordinate):
            return False
        return self.__x == other.get_x() and self.__y == other.get_y()
    
    def __str__(self) -> str:
        """String representation of the coordinates"""
        return "({},{})".format(self.__x,self.__y)
    
    def distance(self, other) -> float:
        """Distance method is used to calculate the distance between two tiles"""
        if not isinstance(other, Coordinate):
            return None
        x_diff = (self.__x - other.get_x()) ** 2
        y_diff = (self.__y - other.get_y()) ** 2
        return (x_diff + y_diff) ** 0.5
    
    def is_in_range(self, other, distance_range) -> bool:
        """Method to check if the distance between two tiles is less than or equal to a certain range (almost equal included)"""
        if not isinstance(other, Coordinate):
            return False
        return self.distance(other) <= distance_range + 1e-6