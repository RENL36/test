from controller.game_controller import GameController
from util.settings import Settings
from util.state_manager import GameState, MenuOptions
from view.menus.menu_view import MenuView
from view.menus.settings_view import SettingsMenu

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
        match MenuOptions(option):
            case MenuOptions.EXIT:
                self.exit()
            case MenuOptions.SETTINGS:
                SettingsMenu(self.settings)
                self.call_menu()
            case MenuOptions.START_GAME:
                self.start_game()
            case MenuOptions.LOAD_GAME:
                # TODO: Implement game load
                pass
            case MenuOptions.RESUME:
                # TODO: Implement game resume
                pass
            case MenuOptions.RESTART:
                # TODO: Implement game restart
                pass
            case MenuOptions.SAVE_GAME:
                # TODO: Implement game save
                pass
    
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