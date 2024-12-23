from collections import defaultdict
from model.game_object import GameObject
from util.coordinate import Coordinate
from model.entity import Entity

"""
This file contains the Map class which is used to represent the map of the game and the methods associated with it.
It serves as the heart of the model-the representation of datas
"""
class Map():
    def __init__(self, size: int):
        """Create a map with a certain size"""
        self.__size: int = size
        self.__matrix: defaultdict[Coordinate, GameObject] = defaultdict( lambda: None )

    def get_size(self) -> int:
        """Method to get the size of the map"""
        return self.__size
    
    def check_placement(self, object: GameObject, coordinate: Coordinate) -> bool:
        """Method to check if an entity can be placed at a certain coordinate"""
        for x in range(object.get_size()):
            for y in range(object.get_size()):
                if not (Coordinate(0, 0) <= Coordinate(coordinate.get_x() + x, coordinate.get_y() + y) <= Coordinate(self.get_size(), self.get_size())):
                    return False
                if self.get(Coordinate(coordinate.get_x() + x, coordinate.get_y() + y)) is not None:
                    return False
        return True

    def add(self, object: GameObject, coordinate: Coordinate):
        """Method to add an entity at a certain coordinate. It also claim other tiles depending on the size."""
        if not self.check_placement(object, coordinate):
            raise ValueError("Cannot place object at the given coordinate.")
        for x in range(object.get_size()):
            for y in range(object.get_size()):
                self.__matrix[Coordinate(coordinate.get_x() + x, coordinate.get_y() + y)]= object

    def remove(self, coordinate: Coordinate) -> GameObject:
        """Method to remove the entity at a certain coordinate. It also remove other tiles depending on the size."""
        if not (Coordinate(0, 0) <= coordinate <= Coordinate(self.get_size(), self.get_size())):
            raise ValueError("Coordinate is out of bounds.")
        object: GameObject = self.__matrix[coordinate]
        if object is None:
            raise ValueError("No entity at the given coordinate.")
        for x in range(object.get_size()):
            for y in range(object.get_size()):
                self.__matrix[Coordinate(coordinate.get_x() + x, coordinate.get_y() + y)]= None
        return object

    def move(self, object: GameObject, new_coordinate: Coordinate):
        """Method to move an entity to a new coordinate"""
        if not object.get_coordinate().is_in_range(new_coordinate, 1):
            raise ValueError("New coordinate is not adjacent to the entity's current coordinate.")
        if not self.check_placement(object, new_coordinate):
            raise ValueError("New coordinate is not available.")
        self.remove(object.get_coordinate())
        self.add(object, new_coordinate)
    
    def get(self, coordinate: Coordinate) -> GameObject:
        """Method to get the entity at a certain coordinate"""
        return self.__matrix[coordinate]
    
    def get_map(self) -> defaultdict[Coordinate, GameObject]:
        """Method to get the map as a matrix"""
        return self.__matrix
    
    def get_map_list(self) -> list[list[GameObject]]:
        """Method to get the map as a list of list"""
        return [ [ self.__matrix[Coordinate(i,j)] for j in range(self.get_size()) ] for i in range(self.get_size()) ]
    
    def get_map_from_to(self, from_coord: Coordinate, to_coord: Coordinate) -> defaultdict[Coordinate, GameObject]:
        """Method to get the map from a certain coordinate to another"""
        map = defaultdict( lambda: None )
        for i in range(from_coord.get_x(), to_coord.get_x() + 1):
            for j in range(from_coord.get_y(), to_coord.get_y() + 1):
                map[Coordinate(i, j)] = self.get(Coordinate(i, j))
        return map
    
    def get_map_list_from_to(self, from_coord: Coordinate, to_coord: Coordinate) -> list[list[GameObject]]:
        """Method to get the map as a list of list from a certain coordinate to another"""
        return [ [ self.get(Coordinate(i,j)) for j in range(from_coord.get_y(), to_coord.get_y() + 1) ] for i in range(from_coord.get_x(), to_coord.get_x() + 1) ]
    
    def __repr__(self):
        """Testing functions"""
        return f"smatrix({repr(self.full_matrix())})"
    
    def __str__(self) -> str:
        """Method to get the matrix of the map"""
        rows = []
        for i in range(self.get_size()):
            row = ""
            for j in range(self.get_size()):
                entity: Entity = self.__matrix[Coordinate(j, i)]
                if entity is None:
                    row += ". "
                else:
                    row += f"{entity.get_letter()} "
            rows.append(row.strip())
        return "\n".join(rows)