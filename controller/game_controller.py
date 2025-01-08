from controller.view_controller import ViewController
from util.map import Map
from util.settings import Settings
from util.state_manager import MapType
import typing
from controller.command import CommandManager, Command, Process
from model.player.player import Player
if typing.TYPE_CHECKING:
    from controller.menu_controller import MenuController
class GameController:
    """This module is responsible for controlling the game."""

    def __init__(self, menu_controller: 'MenuController') -> None:
        """
        Initializes the GameController with the given settings.

        :param menu_controller: The menu controller.
        :type menu_controller: MenuController
        """
        self.__menu_controller: 'MenuController' = menu_controller
        self.settings: Settings = self.__menu_controller.settings
        self.__map: Map = self.__generate_map()
        self.__view_controller: ViewController = ViewController(self)
        self.__running: bool = False
        self.__command_list: list[Command] = []
        self.__players: list[Player] = []
    
    def __generate_map(self) -> Map:
        """
        Generates a map based on the settings.

        :return: The generated map.
        :rtype: Map
        """
        map_generation: Map = Map(self.settings.map_size.value)
        match MapType(self.settings.map_type):
            case MapType.RICH:
                pass
            case MapType.GOLD_CENTER:
                pass
            case MapType.TEST:
                # Generate a test map 10x10 with a town center at (0,0) and a villager at (5,5)
                from util.coordinate import Coordinate
                from model.buildings.town_center import TownCenter
                from model.units.villager import Villager
                map_generation = Map(10)
                town_center = TownCenter()
                coordinate = Coordinate(0,0)
                town_center.set_coordinate(coordinate)
                map_generation.add(town_center, coordinate)
                villager = Villager()
                coordinate = Coordinate(5,5)
                villager.set_coordinate(coordinate)
                map_generation.add(villager, coordinate)
        return map_generation

    def get_map(self) -> Map:
        """
        Returns the map.

        :return: The map.
        :rtype: Map
        """
        return self.__map

    def start(self) -> None:
        """Starts the game."""
        self.__running = True
    
    def pause(self) -> None:
        """Pauses the game."""
        self.__running = False
    
    def exit(self) -> None:
        """Exits the game."""
        self.__running = False
        self.__menu_controller.exit()

    # TODO: Generate list of players and their units/buildings.
    def update(self) -> None:
        """
        Update the game state.
        """
        for command in self.__command_list:
            command.run_command()
        self.__command_list.clear()

    def __assign_command_manager(self) -> None:
        """
        Assign a command manager to all player.

        :param command_manager: The command manager to assign.
        :type command_manager: CommandManager
        """
        for player in self.__players:
            player.set_command_manager(CommandManager(self.__map, player, self.settings.fps, self.__command_list))

