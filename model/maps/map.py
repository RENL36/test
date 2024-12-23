from collections import defaultdict
from model.maps.coordinate import Coordinate
from model.other.entity import Entity

"""
This file contains the Map class which is used to represent the map of the game and the methods associated with it.
"""
class Map():
    def __init__(self, width, height):
        """Used to represent the map of the game."""
        self.__width = width
        self.__height = height
        self.__matrix = defaultdict( lambda: None )
    
    def get_entity(self, coordinate: Coordinate):
        """Method to get the entity at a certain coordinate"""
        return self.__matrix[coordinate]
    
    def add_entity(self, entity: Entity, coordinate: Coordinate):
        """Utilitiy functions, later to move to controller"""
        self.__matrix[coordinate]= entity

    def remove_entity(self, coordinate: Coordinate):
        """Method to remove the entity at a certain coordinate"""
        self.__matrix[coordinate] = None
    
    def __repr__(self):
        """Testing functions"""
        return f"smatrix({repr(self.full_matrix())})"

    def full_matrix(self):
        """Method to get the full matrix of the map"""
        return [ [ self.__matrix[Coordinate(i,j)] for j in range(self.__height) ] for i in range(self.__width) ]
    
    def get_matrix(self):
        """Method to get the matrix of the map"""
        return self.__matrix
    
    def get_width(self):
        """Method to get the width of the map"""
        return self.__width
    
    def get_height(self):
        """Method to get the height of the map"""
        return self.__height
    
    def __str__(self):
        """Method to print the matrix of the map"""
        rows = []
        for i in range(self.__width):
            row = ""
            for j in range(self.__height):
                entity = self.__matrix[Coordinate(i, j)]
                if entity is None:
                    row += ". "
                else:
                    row += f"{entity} "
            rows.append(row.strip())
        return "\n".join(rows)