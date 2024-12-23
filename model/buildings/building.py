from model.entity import Entity

class Building(Entity):
    def __init__(self, name: str, letter: str, hp: int, cost: dict, size: tuple, spawning_time: int):
        """Initializes the building"""
        super.__init__(name, letter, hp, cost, spawning_time)
        super.set_size(size)
        super.set_sprite_path(f"assets/sprites/buildings/{name.lower()}.png")