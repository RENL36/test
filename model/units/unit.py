from model.entity import Entity
import typing
if typing.TYPE_CHECKING:
    from model.resources.resource import Resource

class Unit(Entity):
    def __init__(self, name: str, letter: str, hp: int, cost: dict['Resource', int], spawning_time: int, attack_per_second: int, speed: float):
        super().__init__(name, letter, hp, cost, spawning_time)
        self.__attack_per_second: float = attack_per_second
        self.__speed: float = speed
        super().set_sprite_path(f"assets/sprites/units/{self.get_name().lower()}.png")