from util.map import Map
from util.settings import Settings
from util.state_manager import MapType
from controller.command import CommandManager, Command, Process
from model.player.player import Player
class GameController:
    """This module is responsible for controlling the game."""

    def __init__(self, settings: Settings) -> None:
        """
        Initializes the GameController with the given settings.

        :param settings: The settings for the game.
        :type settings: Settings
        """
        self.settings: Settings = settings
        self.__map: Map = self.__generate_map()
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
                pass
        return map_generation

    #TODO: Generate list of players and their units/buildings.
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

