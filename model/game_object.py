from util.coordinate import Coordinate

class GameObject:
    """This class represents an object in the game."""
    def __init__(self, name: str, letter: str, hp: int):
        self.__name: str = name
        self.__letter: str = letter
        self.__hp: int = hp
        self.__coordinate: Coordinate = None
        self.__alive: bool = True
        self.__size: int = 1
    
    def get_name(self) -> str:
        return self.__name
    
    def get_letter(self) -> str:
        return self.__letter
    
    def damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        if not self.__alive:
            raise ValueError("Entity is already dead")
        if damage >= self.__hp:
            self.__hp = 0
            self.__alive = False
        else:
            self.__hp -= damage
    
    def get_coordinate(self) -> Coordinate:
        return self.__coordinate
    
    def set_coordinate(self, coordinate: Coordinate) -> None:
        self.__coordinate = coordinate

    def is_alive(self) -> bool:
        return self.__alive
    
    def get_size(self) -> int:
        return self.__size

    def __str__(self):
        return (f"{self.__name} ({self.__letter}) - HP : {self.__hp}")