import typing
if typing.TYPE_CHECKING:
    from controller.game_controller import GameController
from model.player.strategy import Strategy
from model.player.player import Player
from util.map import Map
from pygame import time

class AI:
    """This module is responsible for controlling the AI."""
    def __init__(self, player: Player, strategy: 'Strategy', map: Map) -> None:
        """
        Initializes the AI with the given player.

        :param player: The player.
        :type player: Player
        """
        self.__player: Player = player
        self.__strategy: 'Strategy' = Strategy(self)
        self.__map_known: Map = map
        self.__enemies: list[Player] = []

    def update_enemies(self, enemies: list[Player]) -> None:
        """
        Updates the enemies of the AI.

        :param enemies: The enemies.
        :type enemies: list[Player]
        """
        self.__enemies = enemies
    
    def get_enemies(self) -> list[Player]:
        """
        Returns the enemies.

        :return: The enemies.
        :rtype: list[Player]
        """
        return self.__enemies

    def get_player(self) -> Player:
        """
        Returns the player.

        :return: The player.
        :rtype: Player
        """
        return self.__player
    def get_strategy(self) -> 'Strategy':
        """
        Returns the strategy.

        :return: The strategy.
        :rtype: Strategy
        """
        return self.__strategy
    def get_map_known(self) -> Map:
        """
        Returns the map.

        :return: The map.
        :rtype: Map
        """
        return self.__map_known

    def set_player(self, player: Player) -> None:
        """
        Sets the player.

        :param player: The player.
        :type player: Player
        """
        self.__player = player  
    def set_strategy(self, strategy: 'Strategy') -> None:
        """
        Sets the strategy.

        :param strategy: The strategy.
        :type strategy: Strategy
        """
        self.__strategy = strategy

    def set_map_known(self, map: Map) -> None:
        """
        Sets the map.

        :param map: The map.
        :type map: Map
        """
        self.__map_known = map

class AIController:
    """This module is responsible for controlling the AI."""
    def __init__(self, game_controller: 'GameController', refresh_rate: int) -> None:
        """
        Initializes the AIController with the given game controller.

        :param game_controller: The game controller.
        :type game_controller: GameController
        """
        self.__game_controller: 'GameController' = game_controller
        self.__players: list[Player] = self.__game_controller.get_players()
        self.__refresh_rate: int = refresh_rate
        self.__running = True
        for player in self.__players:
            player.set_ai(AI(player, None, self.__game_controller.get_map().capture()))

    def update_knowledge(self) -> None:
        """
        Updates the known map of the player.

        :param player: The player.
        :type player: Player
        """
        for player in self.__players:
            player.get_ai().set_map_known(self.__game_controller.get_map().capture())
            player.get_ai().update_enemies([enemy.capture() for enemy in self.__players if enemy != player])


    def __ai_loop(self) -> None:
        """
        The main loop of the AIController.
        """
        while self.__running:
            for player in self.__players:
                self.update_knowledge(player)
                player.get_ai().get_strategy().execute()
            time.wait(1000*self.__refresh_rate)

    
        