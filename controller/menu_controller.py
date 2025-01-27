from controller.game_controller import GameController
from util.settings import Settings
from util.state_manager import GameState, MenuOptions
from view.menus.load_view import LoadMenu
from view.menus.menu_view import MenuView
from view.menus.settings_view import SettingsMenu
import pickle

class MenuController:
    """Controller for all the menus in the game."""
    
    def __init__(self) -> None:
        """
        Initializes the MenuController with the default state NOT_STARTED and calls the main menu.
        
        :rtype: None
        """
        self.state: GameState = GameState.NOT_STARTED
        self.settings: Settings = Settings()
        self.__menu = MenuView()
        self.__game_controller: GameController = None
        self.call_menu()
    
    def call_menu(self) -> None:
        """
        When called, MenuController will display the main menu based on the current state.
        
        :rtype: None
        """
        option_selected: MenuOptions = self.__menu.show(self.state)
        self.handle_option(option_selected)
    
    def handle_option(self, option: MenuOptions) -> None:
        """
        Handles the option selected by the user.
        
        :param option: The option selected by the user.
        :type option: MenuOptions
        :rtype: None
        """
        option = MenuOptions(option)
        if option == MenuOptions.EXIT:
            self.exit()
        elif option == MenuOptions.SETTINGS:
            SettingsMenu(self.settings)
            self.call_menu()
        elif option == MenuOptions.START_GAME:
            self.start_game()
        elif option == MenuOptions.LOAD_GAME:
            filename = LoadMenu().show()
            if filename is not None:
                self.load_game(filename)
            else:
                self.call_menu()
        elif option == MenuOptions.RESUME:
            # TODO: Implement game resume
            pass
        elif option == MenuOptions.RESTART:
            # TODO: Implement game restart
            pass
        elif option == MenuOptions.SAVE_GAME:
            self.save_game()  
    
    def exit(self) -> None:
        """
        Exits the game.
        
        :rtype: None
        """
        exit(0)

    def start_game(self) -> None:
        """
        Starts a new game by creating a GameController instance.
        
        :rtype: None
        """
        self.state = GameState.PLAYING
        self.__game_controller = GameController(self)
        pass
    
    def save_game(self) -> None:
        """Save the current game state"""
        if self.__game_controller:
            game_state = {
                'settings': self.settings,
                'map': self.__game_controller.get_map(),
                'players': self.__game_controller.get_players(),
            }
        try: 
            filename = "savegame.pkl"
            with open(filename, 'wb') as file:
                pickle.dump(game_state, file)
            print(f"Game successfully saved to {filename}.")
        except Exception as e:
            print(f"Error saving game: {e}")

    def load_game(self, filename: str) -> None:
        """Load a saved game state"""
        try:
            with open(filename, 'rb') as file:
                game_state = pickle.load(file)

            self.settings = game_state['settings']
            self.__game_controller = GameController(self)
            self.__game_controller.load_game(game_state['map'], game_state['players'])
            self.state = GameState.PLAYING
            print("Game successfully loaded.")
        except FileNotFoundError:
            print(f"Save file not found.")
        except Exception as e:
            print(f"Error loading game: {e}")
