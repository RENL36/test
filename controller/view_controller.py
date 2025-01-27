from util.map import Map
from util.settings import Settings
from view.base_view import BaseView
from view.terminal_view import TerminalView
from model.units.villager import Villager
import os, json, typing, webbrowser
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
        """Switch the view."""
        if isinstance(self.__current_view, TerminalView):
            raise NotImplementedError("There is currently only one view.")
        else:
            self.__current_view = TerminalView(self)


    def generate_player_stats(self, player) -> dict:
        """
        Generate a dictionary containing stats for a single player.

        :param player: The player whose stats are being generated.
        :return: A dictionary of player stats.
        """
        return {
            "name": player.get_name(),
            "color": player.get_color(),
            "resources": {
                type(resource).__name__: amount for resource, amount in player.get_resources().items()
            },
            "units": [
                {
                    "name": unit.get_name(),
                    "hp": unit.get_hp(),
                    "attack_per_second": unit.get_attack_per_second(),
                    "speed": unit.get_speed(),

                    # Include inventory if the unit has one (e.g., Villager)
                    "inventory": {
                        type(resource).__name__: amount
                        for resource, amount in getattr(unit, "_Villager__inventory", {}).items()
                    } if isinstance(unit, Villager) else None,
                    "inventory_size": getattr(unit, "_Villager__inventory_size", None) if isinstance(unit, Villager) else None,
                    "collect_time_per_minute": getattr(unit, "_Villager__collect_time_per_minute", None) if isinstance(unit, Villager) else None,
                }
                for unit in player.get_units()
            ],
            "buildings": [
                {
                    "name": building.get_name(),
                    "hp": building.get_hp(),
                    "size": building.get_size(),
                    "cost": {
                        type(resource).__name__: amount for resource, amount in building.get_cost().items()
                    },
                }
                for building in player.get_buildings()
            ],
        }

    def display_stats(self) -> None:
        """
        Pause the game, and create an HTML webpage that shows stats for all players.
        """
        self.pause()
        players = self.__game_controller.get_players()
        all_players_stats = [self.generate_player_stats(player) for player in players]

        # Generate HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Game Stats</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
                .collapsible {{ cursor: pointer; padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; text-align: left; }}
                .content {{ padding: 10px; display: none; background-color: #f9f9f9; border: 1px solid #ccc; border-radius: 5px; }}
            </style>
            <script>
                function toggleContent(id) {{
                    var content = document.getElementById(id);
                    content.style.display = content.style.display === "block" ? "none" : "block";
                }}
            </script>
        </head>
        <body>
            <h1>Game Stats</h1>
            <h2>All Players</h2>
            {self.generate_collapsible_html(all_players_stats)}
        </body>
        </html>
        """

        # Write HTML file
        file_path = os.path.abspath("game_stats.html")
        with open(file_path, "w") as file:
            file.write(html_content)

        # Open in browser
        webbrowser.open(f"file://{file_path}")

    def generate_collapsible_html(self, players_stats: list) -> str:
        """
        Generate collapsible sections for each player's stats.

        :param players_stats: A list of stats for all players.
        :return: An HTML string with collapsible sections.
        """
        html = ""
        for i, player_stats in enumerate(players_stats):
            player_name = player_stats["name"]
            html += f"""
            <button class="collapsible" onclick="toggleContent('player_{i}')">Player: {player_name}</button>
            <div id="player_{i}" class="content">
                <pre>{json.dumps(player_stats, indent=4)}</pre>
            </div>
            """
        return html
