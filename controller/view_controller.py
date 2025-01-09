import threading
from util.map import Map
from util.settings import Settings
from view.base_view import BaseView
from view.terminal_view import TerminalView
from view.two_point_five_view.view2_5d import View2D5
import os , typing , webbrowser


if typing.TYPE_CHECKING:
    from controller.game_controller import GameController

class ViewController:
    def __init__(self, game_controller: 'GameController') -> None:
        """Initialize the view controller."""
        self.__game_controller: 'GameController' = game_controller

        
       

        # Initialiser la vue 2.5D
        self.__view_2_5d: View2D5 = View2D5(self.get_map())

        # Définir la vue actuelle comme la vue terminale
        self.__current_view: BaseView = TerminalView(self)

        # Lancer les vues
        self.start_view()

    def start_view(self) -> None:
        """Start the current view."""
        # Afficher la vue terminale et 2.5D en mode debug (les deux en parallèle)
        threading.Thread(target=self.__terminal_view.show, daemon=True).start()
        threading.Thread(target=self.__view_2_5d.run, daemon=True).start()

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
        """Switch between TerminalView and 2.5D view."""
        try:
            if isinstance(self.__current_view, TerminalView):
                # Arrêter proprement la vue terminale
                print("Switching from TerminalView to View2D5...")
                self.__current_view.exit()  
                
                # Importer et lancer la vue 2.5D
                from view.two_point_five_view.view2_5d import View2D5
                self.__current_view = View2D5(self.get_map())
                self.__current_view.show()
            elif isinstance(self.__current_view, View2D5):
                # Arrêter proprement la vue 2.5D
                print("Switching from View2D5 to TerminalView...")
                self.__current_view.exit() 
                
                # Revenir à la vue Terminal
                self.__current_view = TerminalView(self)
                self.__current_view.show()
            else:
                raise NotImplementedError("The current view is not supported for switching.")
        except Exception as e:
            print(f"Error during view switch: {e}")
            raise

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