from collections import defaultdict
from model.game_object import GameObject
from util.coordinate import Coordinate



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
                self.__matrix[Coordinate(coordinate.get_x() + x, coordinate.get_y() + y)] = object

    def __force_add(self, object: GameObject, coordinate: Coordinate):
        self.__matrix[coordinate] = object

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
    
    def __force_remove(self, coordinate: Coordinate) -> GameObject:
        object: GameObject = self.__matrix[coordinate]
        self.__matrix[coordinate] = None
        return object

    def move(self, object: GameObject, new_coordinate: Coordinate):
        """Method to move an entity to a new adjacent coordinate(8 surrounding coordinates)"""
        if not object.get_coordinate().is_adjacent(new_coordinate):
            raise ValueError("New coordinate is not adjacent to the entity's current coordinate.")
        if not self.check_placement(object, new_coordinate):
            raise ValueError("New coordinate is not available.")
        self.remove(object.get_coordinate())
        self.add(object, new_coordinate)

    def __force_move(self, object: GameObject, new_coordinate: Coordinate):
        self.__force_remove(object.get_coordinate())
        self.__force_add(object, new_coordinate)
    
    def get(self, coordinate: Coordinate) -> GameObject:
        """Method to get the entity at a certain coordinate"""
        return self.__matrix[coordinate]
    
    def get_map(self) -> defaultdict[Coordinate, GameObject]:
        """Method to get the map as a matrix"""
        return self.__matrix
    
    def get_map_list(self) -> list[list[GameObject]]:
        """Method to get the map as a list of list"""
        return [ [ self.__matrix[Coordinate(i,j)] for j in range(self.get_size()) ] for i in range(self.get_size()) ]
    
    def get_from_to(self, from_coord: Coordinate, to_coord: Coordinate) -> 'Map':
        """Method to get the map from a certain coordinate to another as a new Map"""
        map = Map(self.get_size())
        for x in range(from_coord.get_x(), to_coord.get_x() + 1):
            for y in range(from_coord.get_y(), to_coord.get_y() + 1):
                obj = self.get(Coordinate(x, y))
                if obj is not None:
                    map.__force_add(obj, Coordinate(x, y))
        return map
    
    def get_map_from_to(self, from_coord: Coordinate, to_coord: Coordinate) -> defaultdict[Coordinate, GameObject]:
        """Method to get the map from a certain coordinate to another as a matrix"""
        result = defaultdict( lambda: None )
        for x in range(from_coord.get_x(), to_coord.get_x() + 1):
            for y in range(from_coord.get_y(), to_coord.get_y() + 1):
                obj = self.get(Coordinate(x, y))
                if obj is not None:
                    result[Coordinate(x, y)] = obj
        return result
    
    def get_map_list_from_to(self, from_coord: Coordinate, to_coord: Coordinate) -> list[list[GameObject]]:
        """Method to get the map as a list of list from a certain coordinate to another as a list of list"""
        size = self.get_size()
        result = [[ None for _ in range(size) ] for _ in range(size)]
        for x in range(from_coord.get_x(), to_coord.get_x() + 1):
            for y in range(from_coord.get_y(), to_coord.get_y() + 1):
                result[x][y] = self.get(Coordinate(x, y))
        return result
    
    def __repr__(self):
        """Testing functions"""
        return f"smatrix({repr(self.get_map())})"
    
    def __str__(self) -> str:
        """Method to get the matrix of the map with table-like borders"""
        horizontal_line = lambda length: "┌" + "┬".join(["─" * 3] * length) + "┐"
        middle_line = lambda length: "├" + "┼".join(["─" * 3] * length) + "┤"
        bottom_line = lambda length: "└" + "┴".join(["─" * 3] * length) + "┘"
        
        rows = [horizontal_line(self.get_size())]
        for x in range(self.get_size()):
            row = []
            for y in range(self.get_size()):
                object = self.get(Coordinate(x, y))
                row.append(f" {object.get_letter() if object is not None else ' '} ")
            rows.append("│" + "│".join(row) + "│")
            if x < self.get_size() - 1:
                rows.append(middle_line(self.get_size()))
        rows.append(bottom_line(self.get_size()))
        return "\n".join(rows)