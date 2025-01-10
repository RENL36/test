import threading
from util.map import Map
from util.settings import Settings
from view.base_view import BaseView
from view.terminal_view import TerminalView
from view.two_point_five_view.view2_5d import View2D5
import os, typing, webbrowser

if typing.TYPE_CHECKING:
    from controller.game_controller import GameController

class ViewController:
    def __init__(self, game_controller: 'GameController') -> None:
        """Initialize the view controller."""
        self.__game_controller: 'GameController' = game_controller

        # Initialize the terminal view
        self.__terminal_view = TerminalView(self)

        # Initialize the 2.5D view
        self.__view_2_5d = View2D5(self.get_map())

        # Set the current view to TerminalView
        self.__current_view: BaseView = self.__terminal_view

        # Start the initial view
        self.start_view()

    def start_view(self) -> None:
        """Start the current view."""
        try:
            # Start the current view in a separate thread
            threading.Thread(target=self.__current_view.show, daemon=True).start()
        except AttributeError as e:
            print(f"Error starting the view: {e}")

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
                # Stop the terminal view
                print("Switching from TerminalView to View2D5...")
                self.__current_view.exit()

                # Switch to the 2.5D view
                self.__current_view = self.__view_2_5d
                threading.Thread(target=self.__current_view.show, daemon=True).start()
            elif isinstance(self.__current_view, View2D5):
                # Stop the 2.5D view
                print("Switching from View2D5 to TerminalView...")
                self.__current_view.exit()

                # Switch to the terminal view
                self.__current_view = self.__terminal_view
                threading.Thread(target=self.__current_view.show, daemon=True).start()
            else:
                raise NotImplementedError("The current view is not supported for switching.")
        except Exception as e:
            print(f"Error during view switch: {e}")

    def display_stats(self) -> None:
        """
        Pause the game, and create an HTML webpage that shows the current map of the game.
        On hover of a GameObject, show the stats of the GameObject.
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