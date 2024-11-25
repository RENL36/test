class Building:
    def __init__(self, name: str, letter: str, cost: dict[str, int], construction_time: int, health: int, size: int, is_collection_point=False):
        self.name: str = name
        self.letter: str = letter
        self.cost: dict[str, int] = self.__validate_cost(cost)
        self.construction_time: int = construction_time
        self.health: int = health
        self.size: int = size
        self.is_collection_point: bool = is_collection_point
    
    def __validate_cost(self, cost: dict[str, int]):
        valid_keys = { "W" }
        for key in cost.keys():
            if key not in valid_keys:
                raise ValueError(f"Coût en ressource invalide : {key}\nRessource disponible : {valid_keys}")
            
    def __str__(self):
        return (f"{self.name} ({self.letter}) - HP : {self.health}")