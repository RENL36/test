import typing
if typing.TYPE_CHECKING:
    from controller.AI_controller import AI
    from model.player.player import Player
from abc import ABC, abstractmethod
from util.coordinate import Coordinate
#Strategy1
class Strategy(ABC):
    def __init__(self,ai:'AI'):
        self.__ai= ai
    @abstractmethod
    def execute(self):
        pass
    def get_ai(self):
        return self.__ai

class Strategy1(Strategy):
    """
    This is the first strategy
    where player will switch between 2 modes Defend, Attack base on the conditions:
     The difference between the player's number of units and the nearest enemy's number of units
    the nearest enemy is the enemy that is compared by the distance between the player's first building and the enemy's first building (in the list)
    """
    DEFEND = 0
    ATTACK = 1
    def __init__(self,ai: 'AI', unit_difference:int):
        super().__init__(ai)
        self.__unit_difference: int = unit_difference
        self.__mode = self.DEFEND
    def execute(self):
        self.analyse()
        if self.__mode == self.DEFEND:
            self.defend()
        elif self.__mode == self.ATTACK:
            self.attack()

    def analyse(self):
        target_player: 'Player' = self.find_target_player()
        unit_difference: int = self.get_ai().get_player().get_unit_count() - target_player.get_unit_count()
        if self.__unit_difference > unit_difference:
            self.__mode = self.ATTACK
        else:
            self.__mode = self.DEFEND

    def find_target_player(self):
        ai: 'AI' = self.get_ai()
        player: 'Player' = ai.get_player()
        target_player: 'Player' = None
        player_coord: Coordinate = Coordinate(0,0)
        for building in player.get_buildings():
            player_coord = player_coord + building.get_coordinate()
        player_coord = player_coord / len(player.get_buildings())
        target_distance: int = 999999
        for enemy in ai.get_enemies():
            avg_coord: Coordinate = Coordinate(0,0)
            for building in enemy.get_buildings():
                avg_coord = avg_coord + building.get_coordinate()
            avg_coord = avg_coord / len(enemy.get_buildings())
            distance = player_coord.distance(avg_coord)
            if distance < target_distance:
                target_distance = distance
                target_player = enemy
        return target_player

    def defend(self):
        pass

    def attack(self):
        pass