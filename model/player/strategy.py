import typing
if typing.TYPE_CHECKING:
    from controller.AI_controller import AI

from model.player.player import Player
from abc import ABC, abstractmethod
from util.coordinate import Coordinate
from util.map import Map
from controller.command import Task, CollectAndDropTask, MoveTask, KillTask, SpawnTask, BuildTask
from model.units.villager import Villager
from model.units.unit import Unit
from model.buildings.barracks import Barracks
from model.units.swordsman import Swordsman
from model.buildings.town_center import TownCenter
from model.buildings.building import Building
from model.resources.resource import Resource

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
        villagers = [u for u in self.get_ai().get_player().get_units() if isinstance(u, Villager) and u.get_task() is None]
        half_count = (len(villagers) +1) // 2
        center_coordinate = self.get_ai().get_player().get_centre_coordinate()
        build_points = self.get_ai().get_map_known().find_nearest_empty_zones(center_coordinate, TownCenter().get_size())
        collect_points = self.get_ai().get_map_known().find_nearest_objects(center_coordinate, Resource) 
        for i, villager in enumerate(villagers):
            match i% 2:
                case 0:
                    self.collect(villager, collect_points[(i//2) % len(collect_points)])
                case 1:
                    if all(self.get_ai().get_player().get_resources().get(key, 0) >= cost for key, cost in TownCenter().get_cost().items()) and self.get_ai().get_player().get_unit_count() < self.get_ai().get_player().get_max_population():
                        self.build(TownCenter(), villager, build_points[(i//2) % len(build_points)])
                    else:
                        self.collect(villager,collect_points[(i//2) % len(collect_points)])
        town_centers = [b for b in self.get_ai().get_player().get_buildings() if isinstance(b, TownCenter) and b.get_task() is None]
        for town_center in town_centers:
                if all(self.get_ai().get_player().get_resources().get(key, 0) >= cost for key, cost in Villager().get_cost().items()) and self.get_ai().get_player().get_unit_count() < self.get_ai().get_player().get_max_population():
                    self.spawn(town_center)

    def attack(self):
        villagers = [u for u in self.get_ai().get_player().get_units() if isinstance(u, Villager) and u.get_task() is None]
        half_count = (len(villagers) +1) // 2
        center_coordinate = self.get_ai().get_player().get_centre_coordinate()
        build_points = self.get_ai().get_map_known().find_nearest_empty_zones(center_coordinate, Barracks().get_size())
        collect_points = self.get_ai().get_map_known().find_nearest_objects(center_coordinate, Resource) 
        for i, villager in enumerate(villagers):
            match i% 3:
                case 0:
                    self.collect(villager, collect_points[(i//3) % len(collect_points)])
                case 1:
                    if all(self.get_ai().get_player().get_resources().get(key, 0) >= cost for key, cost in Barracks().get_cost().items()):
                        self.build(Barracks(), villager, build_points[(i//3) % len(build_points)])
                    else:
                        self.collect(villager,collect_points[(i//3) % len(collect_points)])
                case 2:
                    if all(self.get_ai().get_player().get_resources().get(key, 0) >= cost for key, cost in TownCenter().get_cost().items()) and self.get_ai().get_player().get_unit_count() < self.get_ai().get_player().get_max_population():
                        self.build(TownCenter(), villager, build_points[(i//3) + 1 % len(build_points)])
                    else:
                        self.collect(villager,collect_points[(i//3) % len(collect_points)])

        swordsmans = [u for u in self.get_ai().get_player().get_units() if isinstance(u, Swordsman) and u.get_task() is None]
        targets = self.get_ai().get_map_known().find_nearest_enemies(self.get_ai().get_player().get_centre_coordinate(), self.__target_player)
        for i, swordsman in enumerate(swordsmans):
            if i < len(targets):
                self.kill(swordsman, targets[i])
            else:
                self.kill(swordsman, targets[0])
        barracks = [b for b in self.get_ai().get_player().get_buildings() if isinstance(b, Barracks) and b.get_task() is None]
        for barrack in barracks:
                if all(self.get_ai().get_player().get_resources().get(key) >= cost for key, cost in Swordsman().get_cost().items()) and self.get_ai().get_player().get_unit_count() < self.get_ai().get_player().get_max_population():
                    self.spawn(barrack)

    def collect(self, villager: Villager, collect_point: Coordinate):
        u = villager
        drop_point = next(( drop_coord for drop_coord in self.get_ai().get_map_known().find_nearest_objects(u.get_coordinate(), Building) if self.get_ai().get_map_known().get(drop_coord).is_resources_drop_point() and self.get_ai().get_map_known().get(drop_coord).get_player() == self.get_ai().get_player() ), None)
        #print(f"Villager {u} is collecting {self.get_ai().get_map_known().get(collect_point)} and dropping at {self.get_ai().get_map_known().get(drop_point)}")
        if drop_point and collect_point: 
            u.set_task(CollectAndDropTask(self.get_ai().get_player().get_command_manager(), u, collect_point, drop_point))

    def build(self, building: Building, villager: Villager, build_point: Coordinate):
        
        task =BuildTask(self.get_ai().get_player().get_command_manager(), villager, build_point, building)
        villager.set_task(task)

    def spawn(self, building: Building):
                task = SpawnTask(self.get_ai().get_player().get_command_manager(), building)
                building.set_task(task)
    
    def kill(self,unit: Unit, target_coord: Coordinate):
        task = KillTask(self.get_ai().get_player().get_command_manager(), unit, target_coord)
        unit.set_task(task)
    