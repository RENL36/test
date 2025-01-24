from controller.view_2_5D_controller import View2_5DController
from util.map import Map
from util.settings import Settings
from view.base_view import BaseView
from view.terminal_view import TerminalView
import os, typing, webbrowser
if typing.TYPE_CHECKING:
    from controller.game_controller import GameController

class ViewController:
    def __init__(self, game_controller: 'GameController') -> None:
        """Initialize the view controller."""
        self.__game_controller: 'GameController' = game_controller
        self.__current_view: BaseView = TerminalView(self)
        self.start_view()
    
    def start_view(self) -> None:
        """Start the view."""
        self.__current_view.show()
    
    def get_map(self) -> Map:
        """Return the map."""
        return self.__game_controller.get_map()
    
    def get_settings(self) -> Settings:
        """Return the settings."""
        return self.__game_controller.settings
    
    def pause(self) -> None:
        """Pause the game."""
        self.__game_controller.pause()
    
    def exit(self) -> None:
        """Exit the game."""
        self.__game_controller.exit()
    
    def switch_view(self) -> None:
        """Bascule entre la vue terminale et la vue 2.5D en appuyant sur F12."""
        if isinstance(self.__current_view, TerminalView):
            print("⏩ Passage à la vue 2.5D...")
            self.__view_2_5D_controller = View2_5DController(self.__settings)
            self.__view_2_5D_controller.launch_view()
            self.__current_view = self.__view_2_5D_controller  # Mise à jour de la vue actuelle
        else:
            print("⏪ Retour à la vue terminale...")
            self.__current_view = TerminalView(self)
            self.start_view()  # Afficher la vue terminale
    
    def display_stats(self) -> None:
        """
        Pause the game, and create an HTML webpage that shows the current map of the game.
        On hover of a GameObject, show the stats of the GameObject.
        For example, if the GameObject is a Unit, shows it's type, health, what it's carrying, etc.
        """
        self.pause()
        webpage = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Game Stats</title>
        </head>
        <body>
            <h1>Game Stats</h1>
            <h2>Map</h2>
            <p>Size: {self.get_map().get_size()}</p>
            <h2>Settings</h2>
            <p>Map Size: {self.get_settings().map_size.value}</p>
            <p>Map Type: {self.get_settings().map_type}</p>
        </body>
        </html>
        """
        with open("game_stats.html", "w") as file:
            file.write(webpage)
        path = os.path.abspath("game_stats.html")
        webbrowser.open(f"file://{path}")