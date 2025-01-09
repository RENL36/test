from controller.game_controller import GameController
from controller.menu_controller import MenuController
from controller.view_controller import ViewController

def main():
    # Initialisez le menu controller
    menu_controller = MenuController()

    # Initialisez le contrôleur du jeu avec le menu_controller
    game_controller = GameController(menu_controller)

    # Créez un contrôleur de vue
    view_controller = ViewController(game_controller)

    # Démarrez la vue
    view_controller.start_view()

if __name__ == "__main__":
    main()