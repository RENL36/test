from blessed import Terminal
from util.state_manager import GameState, MenuOptions

"""
View for the starting screen of the game and the menu (pause).
Used to create, start, load, save a game; change its settings, etc.
Create a menu inside a Terminal window.
"""
class MenuView:
    """Initialize the menu view."""
    def __init__(self) -> None:
        self.current_option: int = 0
        self.term = Terminal()

    """Get the different options available in the menu depending on the game state."""
    def __get_menu_options(self, game_state: GameState) -> list[MenuOptions]:
        if game_state == GameState.NOT_STARTED:
            return [ MenuOptions.START_GAME, MenuOptions.LOAD_GAME, MenuOptions.SETTINGS, MenuOptions.EXIT ]
        elif game_state == GameState.PAUSE:
            return [ MenuOptions.RESUME, MenuOptions.SAVE_GAME, MenuOptions.SETTINGS, MenuOptions.EXIT ]
        elif game_state == GameState.GAME_OVER:
            return [ MenuOptions.RESTART, MenuOptions.LOAD_GAME, MenuOptions.SETTINGS, MenuOptions.EXIT ]

    """Show the menu in the terminal window."""
    def show(self, game_state: GameState) -> int:
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            while True:
                print(self.term.clear)
                options = self.__get_menu_options(game_state)

                print(self.term.center(self.term.bold_red("AIge of EmpAIres")))

                for i, option in enumerate(options):
                    option_str = option.name.replace("_", " ").title()
                    y = 3 + i
                    if i == self.current_option:
                        print(self.term.on_black(self.term.white(f"→ {option_str}")))
                    else:
                        print(f"  {option_str}")

                key = self.term.inkey()

                if key.code == self.term.KEY_UP and self.current_option > 0:
                    self.current_option -= 1
                elif key.code == self.term.KEY_DOWN and self.current_option < len(options) - 1:
                    self.current_option += 1
                elif key.code in [self.term.KEY_ENTER, '\n', '\r']:
                    return options[self.current_option].value

if __name__ == "__main__":
    menu = MenuView()
    selected_option = menu.show(GameState.NOT_STARTED)
    print(f"Selected option: {MenuOptions(selected_option).name}")
