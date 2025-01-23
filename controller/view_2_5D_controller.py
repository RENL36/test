import random
from controller.interactions import Interactions
from model.buildings.town_center import TownCenter
from model.resources.gold import Gold
from model.resources.wood import Wood
from model.units.villager import Villager
from util.coordinate import Coordinate
from util.map import Map
from util.state_manager import MapType
from view.view_2_5D import View2_5D

class View2_5DController:
    """This module is responsible for controlling the 2.5D view game."""

    def __init__(self, settings):
        """
        Initialises the 2.5D controller view with the given settings
        
        :param settings: The settings of the game
        :type settings: Settings
        """
        self.settings: settings = settings
        self.map = self.__generate_map()
        self.view = None


    def launch_view(self):
        """
        Launches the 2.5D view.
        """
        self.view = View2_5D(self.map)
        self.view.run()
    def __generate_players(self, num_players: int, map_generation: Map):
        """
        Generates players for the game.

        :param num_players: Number of players to generate.
        :type num_players: int
        :param map_generation: The game map where players will be placed.
        :type map_generation: Map
        """
        from model.player.player import Player

        self.players = []
        for i in range(num_players):
            player = Player(f"Player {i+1}",'blue')
            self.players.append(player)
    def get_players(self):
        """
        Returns the list of players.
        :return: List of players.
        :rtype: list[Player]
        """
        return self.players

    def __generate_map(self) -> Map:
        """
        Generates a map based on the settings.

        :return: The generated map.
        :rtype: Map
        """
        map_generation = Map(self.settings.map_size.value)
        interactions = Interactions(map_generation)
   
        match MapType(self.settings.map_type):
            
            ## ---- RICH MAP ----
            case MapType.RICH:
                # Ajout de 5% de bois sur la carte
                for _ in range(int(self.settings.map_size.value ** 2 * 0.05)):
                    wood = Wood()
                    while True:
                        coordinate = Coordinate(
                            random.randint(0, self.settings.map_size.value - 1),
                            random.randint(0, self.settings.map_size.value - 1)
                        )
                        if map_generation.check_placement(wood, coordinate):
                            break
                    map_generation.add(wood, coordinate)
                    wood.set_coordinate(coordinate)

                # Ajout de 0.5% d'or de façon aléatoire
                for _ in range(int(self.settings.map_size.value ** 2 * 0.005)):
                    gold = Gold()
                    while True:
                        coordinate = Coordinate(
                            random.randint(0, self.settings.map_size.value - 1),
                            random.randint(0, self.settings.map_size.value - 1)
                        )
                        if map_generation.check_placement(gold, coordinate):
                            break
                    map_generation.add(gold, coordinate)
                    gold.set_coordinate(coordinate)

            ## ---- GOLD CENTER MAP ----
            case MapType.GOLD_CENTER:
                center = Coordinate(self.settings.map_size.value // 2, self.settings.map_size.value // 2)
                radius = int(self.settings.map_size.value * 0.05)

                # Ajout d'un cercle d'or au centre de la carte
                for x in range(center.get_x() - radius, center.get_x() + radius + 1):
                    for y in range(center.get_y() - radius, center.get_y() + radius + 1):
                        if (x - center.get_x()) ** 2 + (y - center.get_y()) ** 2 <= radius ** 2:
                            coordinate = Coordinate(x, y)
                            gold = Gold()
                            map_generation.add(gold, coordinate)
                            gold.set_coordinate(coordinate)

                # Ajout de bois sur 5% de la carte de manière aléatoire
                for _ in range(int(self.settings.map_size.value ** 2 * 0.05)):
                    wood = Wood()
                    while True:
                        coordinate = Coordinate(
                            random.randint(0, self.settings.map_size.value - 1),
                            random.randint(0, self.settings.map_size.value - 1)
                        )
                        if map_generation.check_placement(wood, coordinate):
                            break
                    map_generation.add(wood, coordinate)
                    wood.set_coordinate(coordinate)

            ## ---- TEST MAP ----
            case MapType.TEST:
                map_generation = Map(120)
                interactions = Interactions(map_generation)

                # Création des joueurs
                self.__generate_players(2, map_generation)

                # Ajout de ressources à Player 1
                self.get_players()[0].collect(Wood(), 1000)

                # Initialisation du joueur 1
                town_center1 = TownCenter()
                interactions.place_object(town_center1, Coordinate(0, 0))
                interactions.link_owner(self.get_players()[0], town_center1)
                self.get_players()[0].set_max_population(
                    self.get_players()[0].get_max_population() + town_center1.get_capacity_increase()
                )

                villager1 = Villager()
                interactions.place_object(villager1, Coordinate(5, 5))
                interactions.link_owner(self.get_players()[0], villager1)

                # Ajout d'une tâche de construction pour le villageois 1
                town_center3 = TownCenter()
                #from model.tasks.build_task import BuildTask # type: ignore
                #villager1.set_task(BuildTask(self.get_players()[0].get_command_manager(), villager1, Coordinate(6,6), town_center3))

                # Initialisation du joueur 2
                town_center2 = TownCenter()
                interactions.place_object(town_center2, Coordinate(100, 100))
                interactions.link_owner(self.get_players()[1], town_center2)
                self.get_players()[1].set_max_population(
                    self.get_players()[1].get_max_population() + town_center2.get_capacity_increase()
                )

                villager2 = Villager()
                interactions.place_object(villager2, Coordinate(90, 90))
                interactions.link_owner(self.get_players()[1], villager2)

        return map_generation