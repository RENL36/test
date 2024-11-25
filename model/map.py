from collections import defaultdict
from model.coordinate import Coordinate

"""
This file contains the Map class which is used to represent the map of the game and the methods associated with it.
"""
class Map():
    """Used to represent the map of the game."""
    def __init__(self, width, heigth):
        self.__width = width
        self.__heigth = heigth
        self.__matrix = defaultdict( lambda: None )
    
    """Method to get the entity at a certain coordinate"""
    def get_entity(self, coordinate):
        return self.__matrix[coordinate]
    
    """Utilitiy functions, later to move to controller"""
    def add_entity(self, entity, coordinate):
        self.__matrix[coordinate]= entity

    """Method to remove the entity at a certain coordinate"""
    def remove_entity(self, coordinate):
        self.__matrix[coordinate] = None
    
    """Testing functions"""
    def __repr__(self):
        return f"smatrix({repr(self.full_matrix())})"

    """Method to get the full matrix of the map"""
    def full_matrix(self):
        return [ [ self.__matrix[Coordinate(i,j)] for j in range(self.__height) ] for i in range(self.__width) ]
    
    """Method to get the matrix of the map"""
    def get_matrix(self):
        return self.__matrix
    
    """Method to get the width of the map"""
    def get_width(self):
        return self.__width
    
    """Method to get the height of the map"""
    def get_height(self):
        return self.__height
    
    """Method to print the matrix of the map"""
    def __str__(self):
        for i in range(self.__width):
            row = ""
            for j in range(self.heigth):
                entity = self.__matrix[Coordinate(i, j)]
                if entity is None:
                    row += ". "
                else:
                    row += f"{entity} "
            print(row)