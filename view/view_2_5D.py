import pygame
from util.map import Map
from view.base_view import BaseView
from view.tile_manager import TileManager
from model.player.player import Player
import typing
if typing.TYPE_CHECKING:
    from controller.view_controller import ViewController

class View2_5D(BaseView):
    """
    Main class for 2.5D view.
    """
    def __init__(self, controller: 'ViewController') -> None:
        """Initialize the menu view."""
        super().__init__(controller)
        self.__map: Map = self._BaseView__controller.get_map()

        # Initialisation de Pygame
        pygame.init()
        super().__init__(controller)
        self.width = 1920
        self.height = 1080
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        # self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE | pygame.FULLSCREEN)
        pygame.display.set_caption("2.5D View")
        self.clock = pygame.time.Clock()
        self.running = True
        self.tile_manager = TileManager()    
        self.camera_x = 0
        self.camera_y = 0
        self.camera_speed = 2  # Vitesse de déplacement de la caméra
        self.viewport_width = 20  # Nombre de tuiles affichées horizontalement
        self.viewport_height = 15  # Nombre de tuiles affichées verticalement
        
        # Taille de la carte (en tuiles)
        self.map_size = self.__map.get_size()
        self.tile_size = 40  # Taille d'une tuile
        self.minimap_size = 150  # Taille de la mini-map
        self.minimap_pos = (self.width - self.minimap_size - 10, self.height - self.minimap_size - 10)
        
    def render_map(self):
        """
        Render only the visible part of the map using the camera.
        """
        town_centre = False

        # Chargement de la texture du sol
        grass_block = pygame.transform.scale(pygame.image.load("src/block_aoe.png"), (128, 128))

        # Dessiner toute la carte avec un décalage caméra
        for x in range(self.map_size):
            for y in range(self.map_size):
                iso_x = (x - self.camera_x) * self.tile_size - (y - self.camera_y) * self.tile_size + self.width // 2
                iso_y = (x - self.camera_x) * (self.tile_size // 2) + (y - self.camera_y) * (self.tile_size // 2) + self.height // 4

                self.screen.blit(grass_block, (iso_x, iso_y))

        # Dessiner les objets à leurs positions
        for coordinate, obj in self.__map.get_map().items():
            if not coordinate or not obj: continue

            x, y = coordinate.get_x(), coordinate.get_y()

            iso_x = (x - self.camera_x) * self.tile_size - (y - self.camera_y) * self.tile_size + self.width // 2
            iso_y = (x - self.camera_x) * (self.tile_size // 2) + (y - self.camera_y) * (self.tile_size // 2) + self.height // 4

            if obj.get_letter() == "T" and not town_centre:
                self.screen.blit(
                    pygame.transform.scale(pygame.image.load("src/town_center.png"), (256, 256)),
                    (iso_x, iso_y)
                )
                town_centre = True

            elif obj.get_letter() == "v":
                self.screen.blit(self.tile_manager.get_texture('villager'), (iso_x, iso_y))

            elif obj.get_letter() == "s":
                self.screen.blit(self.tile_manager.get_texture('swordsman'), (iso_x, iso_y))

            elif obj.get_letter() == "h":
                self.screen.blit(self.tile_manager.get_texture('horseman'), (iso_x, iso_y))

            elif obj.get_letter() == "a":
                self.screen.blit(self.tile_manager.get_texture('archer'), (iso_x, iso_y))

            elif obj.get_letter() == "H":
                self.screen.blit(self.tile_manager.get_texture("house"), (iso_x, iso_y))

            elif obj.get_letter() == "C":
                self.screen.blit(self.tile_manager.get_texture("camp"), (iso_x, iso_y))

            elif obj.get_letter() == "B":
                self.screen.blit(self.tile_manager.get_texture("barracks"), (iso_x, iso_y))

            elif obj.get_letter() == "S":
                self.screen.blit(self.tile_manager.get_texture("stable"), (iso_x, iso_y))

            elif obj.get_letter() == "A":
                self.screen.blit(self.tile_manager.get_texture("archery_range"), (iso_x, iso_y))

            elif obj.get_letter() == "K":
                self.screen.blit(self.tile_manager.get_texture("keep"), (iso_x, iso_y))

            elif obj.get_letter() == "W":
                self.screen.blit(self.tile_manager.get_texture("wood"), (iso_x, iso_y))

            elif obj.get_letter() == "F":
                self.screen.blit(self.tile_manager.get_texture("food"), (iso_x, iso_y))

            elif obj.get_letter() == "G":
                self.screen.blit(self.tile_manager.get_texture("gold"), (iso_x, iso_y))
                
            # self.renderer.render_tile(x, y, texture, self.camera)
    
    def render_minimap(self):
        """
        Render a minimap in the bottom-right corner of the screen.
        It shows the entire map with a rectangle indicating the visible area.
        """
        # Définition de la taille et de la position de la mini-map
        minimap_width = 200
        minimap_height = 200
        minimap_x = self.width - minimap_width - 20  # Décalage de 20px du bord droit
        minimap_y = self.height - minimap_height - 20  # Décalage de 20px du bas

        # Dessiner le fond de la mini-map (bordure noire + fond vert)
        pygame.draw.rect(self.screen, (0, 0, 0), (minimap_x - 2, minimap_y - 2, minimap_width + 4, minimap_height + 4))  # Bordure noire
        pygame.draw.rect(self.screen, (34, 139, 34), (minimap_x, minimap_y, minimap_width, minimap_height))  # Fond vert
        
        # Échelle de réduction pour que la carte entière tienne dans la mini-map
        scale_x = minimap_width / self.map_size
        scale_y = minimap_height / self.map_size

        # Dessiner les objets sur la mini-map
        for coordinate, obj in self.__map.get_map().items():
            if not coordinate or not obj: continue

            x, y = coordinate.get_x(), coordinate.get_y()
            pixel_x = int(minimap_x + x * scale_x)
            pixel_y = int(minimap_y + y * scale_y)

            # Couleurs différentes selon les objets
            color = (255, 255, 255)  # Par défaut blanc (terrain)
            if obj.get_letter() == "T":  # Town Center
                color = (255, 215, 0)  # Or
            elif obj.get_letter() == "W":  # Bois
                color = (139, 69, 19)  # Marron
            elif obj.get_letter() == "G":  # Or
                color = (255, 223, 0)  # Jaune
            elif obj.get_letter() == "F":  # Nourriture
                color = (255, 0, 0)  # Rouge
            elif obj.get_letter() == "v":  # Villageois
                color = (0, 0, 255)  # Bleu

            pygame.draw.rect(self.screen, color, (pixel_x, pixel_y, 3, 3))  # Carré de 3x3 pixels

        # Dessiner un rectangle indiquant la zone actuellement visible sur la grande carte
        viewport_x = int(minimap_x + self.camera_x * scale_x)
        viewport_y = int(minimap_y + self.camera_y * scale_y)
        viewport_width = int(self.viewport_width * scale_x)
        viewport_height = int(self.viewport_height * scale_y)

        pygame.draw.rect(self.screen, (255, 0, 0), (viewport_x, viewport_y, viewport_width, viewport_height), 2)  # Rouge pour la position caméra
    
    def show(self) -> None:
        """
        Main loop for the 2.5D view.
        """
        self.__input_loop()
    
    def __input_loop(self) -> None:
        """
        Handle the user input to move the viewport.

        ZQSD or WASD or arrow keys are used to move the viewport.
        MAJ + ZQSD or MAJ + WASD or MAJ + arrow keys are used to move the viewport by 5 cells.
        P is used to pause the game.
        TAB is used to pause the game and display the stats menu.
        ECHAP is used to exit the game.
        F9 is used to take switch view.
        V is used to toggle speed between 1 and 60.

        :return: None
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False  # Quitter proprement
                        pygame.quit()
                    elif event.key == pygame.K_F12:
                        self.running = False
                        self.view_controller.switch_view()

            # Gestion des déplacements de la caméra avec les flèches et touches ZQSD/WASD
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_a]:  # Q, A, ou ←
                self.camera_x = max(0, self.camera_x - self.camera_speed)
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # D ou →
                self.camera_x = min(self.map_size - self.viewport_width, self.camera_x + self.camera_speed)
            if keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_w]:  # Z, W, ou ↑
                self.camera_y = max(0, self.camera_y - self.camera_speed)
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # S ou ↓
                self.camera_y = min(self.map_size - self.viewport_height, self.camera_y + self.camera_speed)
                                            
            # Effacer l'écran et afficher la carte mise à jour
            self.screen.fill((0, 0, 0))
            self.render_map()
            self.render_minimap()
            pygame.display.flip()
            self.clock.tick(self._BaseView__controller.get_settings().fps.value)

        pygame.quit()