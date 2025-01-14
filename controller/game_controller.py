from controller.view_controller import ViewController
from controller.AI_controller import AIController, AI
from util.map import Map
from util.settings import Settings
from util.state_manager import MapType
import typing
from controller.command import CommandManager, Command, TaskManager, BuildTask
from controller.interactions import Interactions
from model.player.player import Player
from model.resources.wood import Wood
from pygame import time
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
        self.__command_list: list[Command] = []
        self.__players: list[Player] = []
        self.__map: Map = self.__generate_map()
        self.__ai_controller: AIController = AIController(self)
        self.__view_controller: ViewController = ViewController(self)
        self.__running: bool = False
        self.__ai_controller.__ai_loop()
        self.game_loop()
        

        
    def __generate_players(self, number_of_player: int, map: Map ) -> None:
        """
        Generates the players based on the settings.
        """
        colors = ["blue", "red", "green", "yellow", "purple", "orange", "pink", "cyan"]
        for i in range(number_of_player):
            player = Player("Player " + str(i+1), colors[i])
            self.get_players().append(player)
            player.set_command_manager(CommandManager(map, player, self.settings.fps.value, self.__command_list))
            player.set_task_manager(TaskManager(player.get_command_manager()))

        
            

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
                map_generation = Map(120)
                interactions = Interactions(map_generation)
                self.__generate_players(2, map_generation) ## always in the creation of a new map, the players are generated before all generation of objects
                self.get_players()[0].collect( Wood(), 1000 )
                ## Init for player 1
                town_center1 = TownCenter()
                interactions.place_object(town_center1, Coordinate(0,0))
                interactions.link_owner(self.get_players()[0], town_center1)
                self.get_players()[0].set_max_population(self.get_players()[0].get_max_population()+town_center1.get_capacity_increase()) ## increase max population

                villager1 = Villager()
                interactions.place_object(villager1, Coordinate(5,5))
                interactions.link_owner(self.get_players()[0], villager1)
                town_center3 = TownCenter()
                villager1.set_task(BuildTask(self.get_players()[0].get_command_manager(), villager1, Coordinate(6,6), town_center3))

                ## Init for player 2
                town_center2 = TownCenter()
                interactions.place_object(town_center2, Coordinate(100,100))
                interactions.link_owner(self.get_players()[1], town_center2)
                self.get_players()[1].set_max_population(self.get_players()[1].get_max_population()+town_center2.get_capacity_increase())

                villager2 = Villager()
                interactions.place_object(villager2, Coordinate(90,90))
                interactions.link_owner(self.get_players()[1], villager2)
        return map_generation
    
## question: what to do if a max_population_increase building is destroyed and the population cap is decreased and become lower than the current unit count?
## possible solution: ban the creation of new units until the population is lower than the new cap but not kill the units already created
    def get_map(self) -> Map:
        """
        Returns the map.
        :return: The map.
        :rtype: Map
        """
        return self.__map
    def get_players(self) -> list[Player]:
        """
        Returns the players.
        :return: The players.
        :rtype: list[Player]
        """
        return self.__players

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
        for command in self.__command_list.copy():
            command.run_command()

    
    def load_task(self) -> None:
        """
        Load the task of the player.
        serves as the player's input
        """
        for player in self.__players:
            player.get_task_manager().execute_tasks()


    def game_loop(self) -> None:
            """
            The main game loop.
            """
            self.start()
            while self.__running:
                self.load_task()
                self.update() 
                # Cap the loop time to ensure it doesn't run faster than the desired FPS
                time.Clock().tick(self.settings.fps.value)


