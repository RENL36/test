from model.game_object import GameObject

class Resource(GameObject):
    def __init__(self, name: str, letter: str, amount: int, spawnable: bool):
        """Initializes the resource"""
        super().__init__(name, letter, 1)
        self.__amount: int = amount
        self.__spawnable: bool = spawnable
        super().set_sprite_path(f"assets/sprites/resources/{self.get_name().lower()}.png")
    
    def get_amount(self) -> int:
        """Returns the amount of the resource"""
        return self.__amount
    
    def is_spawnable(self) -> bool:
        """Returns whether or not the resource can spawn"""
        return self.__spawnable
    
    def collect(self, amount: int) -> int:
        """Collects the resource and returns the amount collected"""
        if amount > self.__amount:
            amount = self.__amount
            super().damage(1)
        self.__amount -= amount
        return amount
    
    def __hash__(self):
        """Allows for the resource to be hashed"""
        return hash(super().get_name())