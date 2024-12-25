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
    
    def distance(self, other: 'Coordinate') -> float:
        """Distance method is used to calculate the euclidian between two tiles"""
        if not isinstance(other, Coordinate):
            return None
        return ((self.get_x() - other.get_x())**2 + (self.get_y() - other.get_y())**2)**0.5
    
    def is_in_range(self, other: 'Coordinate', distance_range: float) -> bool:
        """Method to check if the distance between two tiles is less than or equal to a certain range (almost equal included), diagonal tiles included"""
        if not isinstance(other, Coordinate):
            return False
        return self.distance(other) <= distance_range + 1e-16
    
    def is_adjacent(self, other: 'Coordinate') -> bool:
        """Method to check if two tiles are adjacentt (diagonal tiles included)"""
        if not isinstance(other, Coordinate):
            return False
        return self != other and self.is_in_range(other, 2**0.5)
    
    def __hash__(self) -> int:
        """Hash for the coordinates to be read by the dictionary"""
        return hash((self.get_x(), self.get_y()))
    
    def __eq__(self, other: object) -> bool:
        """Equality check for the coordinates"""
        if not isinstance(other, Coordinate):
            return False
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()
    
    def __lt__(self, other: 'Coordinate') -> bool:
        """
        Less than comparison between two coordinates. (Symbol: <)

        Is less than all the coordinates where the following conditions are all true:
        - self.get_x() is less than other.get_x()
        - self.get_y() is less than other.get_y()
        """
        if not isinstance(other, Coordinate):
            return False
        return self.get_x() < other.get_x() and self.get_y() < other.get_y()
    
    def __le__(self, other: 'Coordinate') -> bool:
        """
        Less than or equal to comparison between two coordinates. (Symbol: <=)

        Is less than or equal to all the coordinates where the following conditions are all true:
        - self.get_x() is less than or equal to other.get_x()
        - self.get_y() is less than or equal to other.get_y()
        """
        if not isinstance(other, Coordinate):
            return False
        return self.get_x() <= other.get_x() and self.get_y() <= other.get_y()

    def __gt__(self, other: 'Coordinate') -> bool:
        """
        Greater than comparison between two coordinates. (Symbol: >)

        Is greater than all the coordinates where the following conditions are all true:
        - self.get_x() is greater than other.get_x()
        - self.get_y() is greater than other.get_y()
        """
        if not isinstance(other, Coordinate):
            return False
        return self.get_x() > other.get_x() and self.get_y() > other.get_y()
    
    def __ge__(self, other: 'Coordinate') -> bool:
        """
        Greater than or equal to comparison between two coordinates. (Symbol: >=)

        Is greater than or equal to all the coordinates where the following conditions are all true:
        - self.get_x() is greater than or equal to other.get_x()
        - self.get_y() is greater than or equal to other.get_y()
        """
        if not isinstance(other, Coordinate):
            return False
        return self.get_x() >= other.get_x() and self.get_y() >= other.get_y()

    def __add__(self, other: 'Coordinate') -> 'Coordinate':
        """Addition of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() + other, self.get_y() + other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() + other.get_x(), self.get_y() + other.get_y())
    
    def __sub__(self, other: 'Coordinate') -> 'Coordinate':
        """Subtraction of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() - other, self.get_y() - other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() - other.get_x(), self.get_y() - other.get_y())
    
    def __mul__(self, other: 'Coordinate') -> 'Coordinate':
        """Multiplication of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() * other, self.get_y() * other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() * other.get_x(), self.get_y() * other.get_y())
    
    def __truediv__(self, other: 'Coordinate') -> 'Coordinate':
        """Division of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() / other, self.get_y() / other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() / other.get_x(), self.get_y() / other.get_y())
    
    def __floordiv__(self, other: 'Coordinate') -> 'Coordinate':
        """Floor division of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() // other, self.get_y() // other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() // other.get_x(), self.get_y() // other.get_y())
    
    def __mod__(self, other: 'Coordinate') -> 'Coordinate':
        """Modulus of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() % other, self.get_y() % other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() % other.get_x(), self.get_y() % other.get_y())
    
    def __pow__(self, other: 'Coordinate') -> 'Coordinate':
        """Power of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() ** other, self.get_y() ** other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() ** other.get_x(), self.get_y() ** other.get_y())
    
    def __lshift__(self, other: 'Coordinate') -> 'Coordinate':
        """Left shift of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() << other, self.get_y() << other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() << other.get_x(), self.get_y() << other.get_y())
    
    def __rshift__(self, other: 'Coordinate') -> 'Coordinate':
        """Right shift of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() >> other, self.get_y() >> other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() >> other.get_x(), self.get_y() >> other.get_y())
    
    def __and__(self, other: 'Coordinate') -> 'Coordinate':
        """Bitwise and of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() & other, self.get_y() & other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() & other.get_x(), self.get_y() & other.get_y())
    
    def __xor__(self, other: 'Coordinate') -> 'Coordinate':
        """Bitwise xor of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() ^ other, self.get_y() ^ other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() ^ other.get_x(), self.get_y() ^ other.get_y())
    
    def __or__(self, other: 'Coordinate') -> 'Coordinate':
        """Bitwise or of a coordinate with another coordinate or an integer"""
        if isinstance(other, int):
            return Coordinate(self.get_x() | other, self.get_y() | other)
        if not isinstance(other, Coordinate):
            return None
        return Coordinate(self.get_x() | other.get_x(), self.get_y() | other.get_y())
    
    def __neg__(self) -> 'Coordinate':
        """Negation of the coordinates"""
        return Coordinate(-self.get_x(), -self.get_y())
    
    def __pos__(self) -> 'Coordinate':
        """Positive of the coordinates"""
        return Coordinate(+self.get_x(), +self.get_y())
    
    def __abs__(self) -> 'Coordinate':
        """Absolute value of the coordinates"""
        return Coordinate(abs(self.get_x()), abs(self.get_y()))
    
    def __invert__(self) -> 'Coordinate':
        """Invert the coordinates"""
        return Coordinate(~self.get_x(), ~self.get_y())
    
    def __str__(self) -> str:
        """String representation of the coordinates"""
        return f"({self.get_x()},{self.get_y()})"

    def __repr__(self) -> str:
        """Representation of the coordinates"""
        return f"Coordinate({self.get_x()}, {self.get_y()})"