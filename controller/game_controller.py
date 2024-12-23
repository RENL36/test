from util.map import Map
from util.settings import Settings
from util.state_manager import MapType

"""
This module is responsible for controlling the game.
"""
class GameController:
    def __init__(self, settings: Settings) -> None:
        """Initializes the GameController with the given settings."""
        self.settings: Settings = settings
        self.__map: Map = self.__generate_map()
    
    def __generate_map(self) -> Map:
        """Generates a map based on the settings."""
        map_generation: Map = Map(self.settings.map_size.value, self.settings.map_size.value)
        match MapType(self.settings.map_type):
            case MapType.RICH:
                pass
            case MapType.GOLD_CENTER:
                pass
            case MapType.TEST:
                pass
        return map_generation
