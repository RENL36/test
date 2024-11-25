"""
This file contains the Coordinate class which is used to represent the coordinates of the tiles in the grid and the methods associated with it.
"""

class Coordinate:
    """Used to represent the coordinates of the tiles in the grid."""
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
    
    """Setter method for the x coordinate"""
    def set_x(self, x: int):
        self.__x = x
    
    """Setter method for the y coordinate"""
    def set_y(self, y: int):
        self.__y = y
    
    """Getter method for the x coordinate"""
    def get_x(self) -> int:
        return self.__x
    
    """Getter method for the y coordinate"""
    def get_y(self) -> int:
        return self.__y

    """Hash for the coordinates to be read by the dictionary"""
    def __hash__(self):
        return hash((self.__x, self.__y))
    
    """"Equality check for the coordinates"""
    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y
    
    """String representation of the coordinates"""
    def __str__(self):
        return "({},{})".format(self.__x,self.__y)
    
    """Distance method is used to calculate the distance between two tiles"""
    def distance(self, other):
        x_diff = (self.__x - other.x) ** 2
        y_diff = (self.__y - other.y) ** 2
        return (x_diff + y_diff) ** 0.5
    
    """Distance method is used to calculate the distance between two tiles in the x direction"""
    def distance_x(self, other):
        x_diff = (self.__x - other.x) ** 2
        return (x_diff) ** 0.5
    
    """Distance method is used to calculate the distance between two tiles in the y direction"""
    def distance_y(self, other):
        y_diff = (self.__y - other.y) ** 2
        return (y_diff) ** 0.5
    
    """Method to check if the distance between two tiles is less than or equal to a certain range (almost equal included)"""
    def is_in_range(self, other, distance_range):
        return self.distance(other) <= distance_range + 1e-6