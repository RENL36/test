from model.game_object import GameObject

class Resource(GameObject):
    def __init__(self, name: str, letter: str, amount: int, spawnable: bool):
        """Initializes the resource"""
        super.__init__(name, letter, 1)
        self.amount: int = amount
        super.set_sprite_path(f"assets/sprites/resources/{name.lower()}.png")
    
    def get_amount(self) -> int:
        """Returns the amount of the resource"""
        return self.amount
    
    def is_spawnable(self) -> bool:
        """Returns whether or not the resource can spawn"""
        return self.spawnable
    
    def collect(self, amount: int) -> int:
        """Collects the resource and returns the amount collected"""
        if amount > self.amount:
            amount = self.amount
            self.damage(1)
        self.amount -= amount
        return amount
    
    def __hash__(self):
        """Allows for the resource to be hashed"""
        return hash(super.get_name())