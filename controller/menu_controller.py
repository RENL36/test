from controller.game_controller import GameController
from controller.view_2_5D_controller import View2_5DController
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
        option = MenuOptions(option)
        if option == MenuOptions.EXIT:
            self.exit()
        elif option == MenuOptions.SETTINGS:
            SettingsMenu(self.settings)
            self.call_menu()
        elif option == MenuOptions.START_GAME:
            self.start_game()
        elif option == MenuOptions.LOAD_GAME:
            # TODO: Implement game load
            pass
        elif option == MenuOptions.RESUME:
            # TODO: Implement game resume
            pass
        elif option == MenuOptions.RESTART:
            # TODO: Implement game restart
            pass
        elif option == MenuOptions.SAVE_GAME:
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

    def start_2_5D_view(self) -> None:
        """
        Starts a new game by creating a View2_5DController instance

        :rtype: None
        """
        self.state = GameState.PLAYING
        self.__game_controller = View2_5DController(self.settings)
        self.__game_controller.launch_view()
        # return to the main menu after the 2.5D view is closed
        self.call_menu()    