from model.maps.coordinate import Coordinate

class Resource:
    def __init__(self, name: str, letter: str, amount: int, spawnable: bool):
        self.name: str = name
        self.letter: str = letter
        self.amount: int = amount
        self.spawnable: bool = spawnable
        self.__cordinate = None

    """"""    
    def __str__(self):
        return f"{self.name} ({self.letter}) - Amount: {self.amount}"
    
    """Get the coordinate of the resource"""
    def get_coordinate(self):
        return self.__cordinate
    
    """Set the coordinate of the resource"""
    def set_coordinate(self, coordinate: Coordinate):
        self.__cordinate = coordinate

    """Get the name of the resource"""
    def get_letter(self):
        return self.__letter

    """Get the amount of the resource"""
    def get_amount(self):
        return self.__amount
    
      
