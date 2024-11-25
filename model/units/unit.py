class Unit:
    def __init__(self, name: str, letter: str, hp: int, attack_per_second: int, speed: float, cost: dict[str, int], training_time: int):
        self.__name: str = name
        self.__letter: str = letter
        self.__hp: int = hp
        self.__attack_per_second: float = attack_per_second
        self.__speed: float = speed
        self.__cost = self.__validate_cost(cost)
        self.__training_time: int = training_time
        self.__sprite_path: str = f"assets/sprites/units/{name.lower()}.png"

    def __validate_cost(self, cost: dict[str, int]):
        valid_keys = { "F", "G" }
        for key in cost.keys():
            if key not in valid_keys:
                raise ValueError(f"Coût en ressource invalide : {key}\nRessource disponible : {valid_keys}")

    def __str__(self):
        return (f"{self.__name} ({self.__letter}) - HP : {self.__hp}")