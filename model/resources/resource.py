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
    
    """Create a resource on the map""" 
    def create(self, map, coordinate: Coordinate):
        map.create_entity(self, coordinate)

    """Destroy a resource on the map"""
    def destroy(self, map):
        map.destroy_entity(self)

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
    
    """Method to manage the resource"""
    def manage_ressource(self, action: str, value: int):

        """Manage the resource based on the action.
        
        For action, two possibilites :
        "add" to add ressource
        "consume" to consume ressource
        
        """

        if action == "add":
            self.amount += value
            print(f"Ajout de {self.name}, Quantité : {value}")
        elif action == "consume":
            if self.amount >= value:
                self.amount -= value
                print(f"Consommation de {self.name}, Quantité : {value}")
            else:
                print(f"Erreur de Ressource :{self.name} insuffisante. Disponible :{self.amount} ")
        else:
            print(f"Action {action} non reconnue")        
