from util.map import Map
from util.settings import Settings
from view.base_view import BaseView
from view.terminal_view import TerminalView

class ViewController:
    def __init__(self, map: Map, settings: Settings) -> None:
        """Initialize the view controller."""
        self.__map = map
        self.__settings = settings
        self.__current_view: BaseView = TerminalView(self)
        self.start_view()
    
    def start_view(self) -> None:
        """Start the view."""
        self.__current_view.show()
    
    def get_map(self) -> Map:
        """Return the map."""
        return self.__map
    
    def get_settings(self) -> Settings:
        """Return the settings."""
        return self.__settings