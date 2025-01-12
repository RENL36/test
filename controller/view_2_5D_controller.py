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
                coordinate = Coordinate(0, 0)
                town_center.set_coordinate(coordinate)
                map_generation.add(town_center, coordinate)
                villager = Villager()
                coordinate = Coordinate(5,5)
                villager.set_coordinate(coordinate)
                map_generation.add(villager, coordinate)
        return map_generation