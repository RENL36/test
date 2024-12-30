from controller.interactions import Interactions
from util.map import Map
from model.player.player import Player
from model.game_object import GameObject
from model.units.unit import Unit
from util.coordinate import Coordinate
from model.resources.resource import Resource
from model.units.villager import Villager
from model.buildings.building import Building
from model.entity import Entity
from enum import Enum
from abc import ABC, abstractmethod

class Process(Enum):
    """This class is responsible for storing the processes that can be executed."""
    SPAWN = 0
    MOVE = 1
    ATTACK = 2
    COLLECT = 3
    DROP = 4
    BUILD = 5
class SpawningTime(dict[str, int]):
    """This class is responsible for storing the normal time it takes to spawn an entity ."""
    def __init__(self) -> None:
        
        self["House"] = 25
        self["Town Center"] = 150  
        self["Villager"] = 25

class UnitSpawner(dict[str, Unit]):
    """This class is responsible for storing the unit spawner."""
    def __init__(self) -> None:
        self["Town Center"] = Villager()
class Command(ABC):
    """This class is responsible for executing commands."""

    def __init__(self, map: Map, player: Player, entity: Entity, process: Process, convert_coeff: int ) -> None:
        """
        Initializes the Command with the given map, player, entity, process and convert_coeff.
        param map: The map where the command will be executed.
        :type map: Map
        :param player: The player that will execute the command.
        :type player: Player
        :param entity: The entity that will execute the command.
        :type entity: Entity
        :param process: The process that the command will execute.
        :type process: Process
        :param convert_coeff: The coefficient used to convert time to tick.
        :type convert_coeff: int

        """
        self.__interactions: Interactions = Interactions(map)
        self.__process: Process = process
        self.__player: Player = player
        self.__entity: Entity = entity
        self.__convert_coeff: int = convert_coeff
        self.__time: float = 0
        self.__tick: int = 0
    
    def get_tick(self) -> int:
        """
        Returns the tick of the command.
        :return: The tick of the command.
        :rtype: int
        """
        return self.__tick
    def set_tick(self, tick: int) -> None:
        """
        Sets the tick of the command.
        :param tick: The tick of the command.
        :type tick: int
        """
        self.__tick = tick
    
    def get_time(self) -> float:
        """
        Returns the time of the command.
        :return: The time of the command.
        :rtype: float
        """
        return self.__time
    
    def set_time(self, time: float) -> None:
        """
        Sets the time of the command.
        :param time: The time of the command.
        :type time: float
        """
        self.__time = time
    
    def get_entity(self) -> Entity:
        """
        Returns the entity that will execute the command.
        :return: The entity that will execute the command.
        :rtype: Entity
        """
        return self.__entity
    
    def get_process(self) -> Process:
        """
        Returns the process that the command will execute.
        :return: The process that the command will execute.
        :rtype: Process
        """
        return self.__process
    
    def get_player(self):
        """
        Returns the player that will execute the command.
        :return: The player that will execute the command.
        :rtype: Player
        """
        return self.__player

    def push_command_to_list(self, command_list: list['Command']) -> None:
        """
        Pushes the command to the given list.
        :param command_list: The list where the command will be pushed.
        :type command_list: list
        """
        for command in command_list:
            if command.get_entity() == self.__entity and not (command.get_process() = Process.SPAWN):
                if command.get_process() == Process.COLLECT or command.get_process() == Process.BUILD:
                    raise ValueError("Entity is already collecting or building.")
                if (command.get_process() == Process.ATTACK or command.get_process() == Process.MOVE) and command.get_process() == self.__process:
                    raise ValueError("Entity is cooling down from attacking or moving.")
        
        command_list.append(self)
    
    def remove_command_from_list(self, command_list: list['Command']) -> None:
        """
        Removes the command from the given list.
        :param command_list: The list where the command will be removed.
        :type command_list: list
        """
        command_list.remove(self)
    def __eq__(self, other: 'Command') -> bool:
        """
        Compares the command with another command.
        :param other: The other command to compare.
        :type other: Command
        :return: True if the commands are equal, False otherwise.
        :rtype: bool
        """
        return self.__entity == other.get_entity() and self.__process == other.get_process()
    @abstractmethod
    def run_command(self):
        """
        Runs the command.
        This method must be implemented by the subclasses.
        """
        pass
    

class SpawnCommand(Command):
    """This class is responsible for executing spawn commands."""

    def __init__(self, map: Map, player: Player, building: Building, target_coord: Coordinate, convert_coeff: int, command_list: list[Command]) -> None:
        """
        Initializes the SpawnCommand with the given map, player, building, target_coord and convert_coeff.
        :param map: The map where the command will be executed
        :type map: Map
        :param player: The player that will execute the command.
        :type player: Player
        :param building: The building that will execute the command.
        :type building: Building
        :param target_coord: The target coordinate where the entity will be spawned.
        :type target_coord: Coordinate
        :param convert_coeff: The coefficient used to convert time to tick.
        :type convert_coeff: int
        """
        super().__init__(map, player, building, Process.SPAWN, convert_coeff)
        self.set_time(SpawningTime()[UnitSpawner()[building.get_name()].get_name])
        self.set_tick(self.get_time() * convert_coeff)
        self.__target_coord = target_coord
        self.__command_list = command_list
        super().push_command_to_list(command_list)

    def run_command(self):
        """
        Runs the spawn command.
        """
        if self.get_tick() == self.__convert_coeff * self.get_time():
            if self.get_player().get_unit_count() >= self.get_player().get_max_population():
                super().remove_command_from_list()
                raise ValueError("Population limit reached.")
            if not all(self.get_player().check_consume(resource, amount) for resource, amount in UnitSpawner()[self.get_entity().get_name()].get_cost().items()):
                super().remove_command_from_list()
                raise ValueError("Not enough resources.")
            for resource, amount in UnitSpawner()[self.get_entity().get_name()].get_cost().items():
                self.get_player().consume(resource, amount)
            place_holder: GameObject = GameObject("Place Holder",'x',0)
            self.__interactions.place_object(place_holder, self.__target_coord)
        
        if self.get_tick() > 0:
            self.set_tick(self.get_tick() - 1)
        else:
            self.__interactions.remove_object(place_holder)
            spawned: Unit = UnitSpawner()[self.get_entity().get_name()]
            self.__interactions.place_object(spawned, self.__target_coord)
            self.get_player().add_unit(spawned)
            super().remove_command_from_list(self.__command_list)

class MoveCommand(Command):
    """This class is responsible for executing move commands."""
    
    def __init__(self, map: Map, player: Player, unit: Unit, target_coord: Coordinate, convert_coeff: int, command_list: list[Command]) -> None:
        """
        Initializes the MoveCommand with the given map, player, entity, process and convert_coeff.
        :param map: The map where the command will be executed.
        :type map: Map
        :param unit: The entity that will execute the command.
        :type unit: Unit
        :param process: The process that the command will execute.
        :type process: Process
        :param convert_coeff: The coefficient used to convert time to tick.
        :type convert_coeff: int
        """
        super().__init__(map, player, unit, Process.MOVE, convert_coeff)
        self.set_time(unit.get_speed())
        self.set_tick(self.get_time() * convert_coeff)
        self.__target_coord = target_coord
        self.__command_list = command_list
        super().push_command_to_list(command_list)
    
    def run_command(self):
        """
        Runs the move command.
        """
        if self.get_tick() == self.__convert_coeff * self.get_time():
            self.__interactions.move_unit(self.get_entity(), self.__target_coord)
        if self.get_tick() > 0:
            self.set_tick(self.get_tick() - 1)
        else:
            super().remove_command_from_list(self.__command_list)
    
class AttackCommand(Command):
    """This class is responsible for executing attack commands."""
    
    def __init__(self, map: Map, player: Player, unit: Unit, target_coord: Coordinate, convert_coeff: int, command_list: list[Command]) -> None:
        """
        Initializes the AttackCommand with the given map, player, entity, process and convert_coeff.
        :param map: The map where the command will be executed
        :type map: Map
        :param player: The player that will execute the command.
        :type player: Player
        :param unit: The entity that will execute the command.
        :type unit: Unit
        :param target_coord: The target coordinate where the entity will attack.
        :type target_coord: Coordinate
        :param convert_coeff: The coefficient used to convert time to tick.
        :type convert_coeff: int
        """
        super().__init__(map, player, unit, Process.ATTACK, convert_coeff)
        self.set_time(1)
        self.set_tick(self.get_time() * convert_coeff)
        self.__target_coord = target_coord
        self.__command_list = command_list
        super().push_command_to_list(command_list)
    
    def run_command(self):
        """
        Runs the attack command.
        """
        if self.get_tick() == self.__convert_coeff * self.get_time():
            self.__interactions.attack(self.get_entity(), self.__target_coord)
        if self.get_tick() > 0:
            self.set_tick(self.get_tick() - 1)
        else:
            super().remove_command_from_list(self.__command_list)

class CollectCommand(Command):
    """This class is responsible for executing collect commands."""
    
    def __init__(self, map: Map, player: Player, unit: Villager, target_coord: Coordinate, convert_coeff: int, command_list: list[Command]) -> None:
        """
        Initializes the CollectCommand with the given map, player, entity, process and convert_coeff.
        :param map: The map where the command will be executed
        :type map: Map
        :param player: The player that will execute the command.
        :type player: Player
        :param unit: The entity that will execute the command.
        :type unit: Unit
        :param target_coord: The target coordinate where the entity will collect.
        :type target_coord: Coordinate
        :param convert_coeff: The coefficient used to convert time to tick.
        :type convert_coeff: int
        """
        super().__init__(map, player, unit, Process.COLLECT, convert_coeff)
        self.set_time(25.0/60)
        self.set_tick(self.get_time() * convert_coeff)
        self.__target_coord = target_coord
        self.__command_list = command_list
        super().push_command_to_list(command_list)
    
    def run_command(self):
        """
        Runs the collect command.
        """
        if self.get_tick() > 0:
            self.set_tick(self.get_tick() - 1)
        else:
            self.__interactions.collect_resource(self.get_entity(), self.__target_coord, 1)
            super().remove_command_from_list(self.__command_list)

class DropCommand(Command):
    """This class is responsible for executing drop commands."""
    
    def __init__(self, map: Map, player: Player, unit: Villager, target_coord: Coordinate, convert_coeff: int, command_list: list[Command]) -> None:
        """
        Initializes the DropCommand with the given map, player, entity, process and convert_coeff.
        :param map: The map where the command will be executed
        :type map: Map
        :param player: The player that will execute the command.
        :type player: Player
        :param unit: The entity that will execute the command.
        :type unit: Unit
        :param target_coord: The target coordinate where the entity will drop.
        :type target_coord: Coordinate
        :param convert_coeff: The coefficient used to convert time to tick.
        :type convert_coeff: int
        """
        super().__init__(map, player, unit, Process.DROP, convert_coeff)
        
    def run_command(self):
        """
        Runs the drop command.
        """
        self.__interactions.drop_resource(self.get_player(), self.get_entity(), self.__target_coord)
    
class BuildCommand(Command):
    """This class is responsible for executing build commands."""
    
    def __init__(self, map: Map, player: Player, unit: Villager, building: Building, target_coord: Coordinate, convert_coeff: int, command_list: list[Command]) -> None:
        """
        Initializes the BuildCommand with the given map, player, entity, process and convert_coeff.
        :param map: The map where the command will be executed
        :type map: Map
        :param player: The player that will execute the command.
        :type player: Player
        :param unit: The entity that will execute the command.
        :type unit: Unit
        :param building: The building that will be built.
        :type building: Building
        :param target_coord: The target coordinate where the entity will build.
        :type target_coord: Coordinate
        :param convert_coeff: The coefficient used to convert time to tick.
        :type convert_coeff: int
        """
        super().__init__(map, player, unit, Process.BUILD, convert_coeff)
        self.set_time(SpawningTime()[building.get_name()])
        self.set_tick(self.get_time() * convert_coeff)
        self.__building = building
        self.__target_coord = target_coord
        self.__command_list = command_list
        super().push_command_to_list(command_list)

    def run_command(self):
        """
        Runs the build command.
        """
        if not self.get_entity().get_coordinate().is_adjacent(self.__target_coord):
            super().remove_command_from_list()
            raise ValueError("Target is out of range.")
        # To do: implement multi-build and another adjacent check
        if self.get_tick() == self.__convert_coeff * self.get_time():
            if not all(self.get_player().check_consume(resource, amount) for resource, amount in self.__building.get_cost().items()):
                super().remove_command_from_list()
                raise ValueError("Not enough resources.")
            for resource, amount in self.__building.get_cost().items():
                self.get_player().consume(resource, amount)
            place_holder: GameObject = GameObject("Place Holder",'x',0)
            self.__interactions.place_object(place_holder, self.__target_coord)
        
        if self.get_tick() > 0:
            self.set_tick(self.get_tick() - 1)
        else:
            self.__interactions.remove_object(place_holder)
            self.__interactions.place_object(self.__building, self.__target_coord)
            self.get_player().add_building(self.__building)
            super().remove_command_from_list(self.__command_list)


class CommandManager:
    """This class is responsible for managing commands of a single player, using the same list of commands for all players."""

    def __init__(self, map: Map, player: Player, convert_coeff: int, command_list: list[Command]) -> None:
        """
        Initializes the CommandManager with the given map, player and convert_coeff.
        :param map: The map where the command will be executed.
        :type map: Map
        :param player: The player that will execute the command.
        :type player: Player
        :param convert_coeff: The coefficient used to convert time to tick.
        :type convert_coeff: int
        """
        self.__map: Map = map
        self.__player: Player = player
        self.__convert_coeff: int = convert_coeff
        self.__command_list: list[Command] = command_list
    
    def command(self, entity: Entity, process: Process, target_coord: Coordinate, building: Building = None ) -> None:
        """
        Creates a command with the given entity, process and target coordinate.
        :param entity: The entity that will execute the command.
        :type entity: Entity
        :param process: The process that the command will execute.
        :type process: Process
        :param target_coord: The target coordinate where the entity will execute the command.
        :type target_coord: Coordinate
        :param building: The building that will be built. It is only used when the process is Process.BUILD, otherwise it is None.   
        :type building: Building
        """
        if process == Process.SPAWN:
            SpawnCommand(self.__map, self.__player, entity, target_coord, self.__convert_coeff, self.__command_list)
        elif process == Process.MOVE:
            MoveCommand(self.__map, self.__player, entity, target_coord, self.__convert_coeff, self.__command_list)
        elif process == Process.ATTACK:
            AttackCommand(self.__map, self.__player, entity, target_coord, self.__convert_coeff, self.__command_list)
        elif process == Process.COLLECT:
            CollectCommand(self.__map, self.__player, entity, target_coord, self.__convert_coeff, self.__command_list)
        elif process == Process.DROP:
            DropCommand(self.__map, self.__player, entity, target_coord, self.__convert_coeff, self.__command_list)
        elif process == Process.BUILD:
            BuildCommand(self.__map, self.__player, entity, building, target_coord, self.__convert_coeff, self.__command_list)
    

