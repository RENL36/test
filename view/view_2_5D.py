import pygame
# from .camera import Camera
# from .renderer import Renderer
from .tile_manager import TileManager

class View2_5D:
    """
    Main class for 2.5D view.
    """

    def __init__(self, game_map):
        """
        Initialises the 2.5D view.

        :param game_map: Instance of the game map
        """
        pygame.init()

        self.width = 1600
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2.5D View")

        self.clock = pygame.time.Clock()
        self.running = True
        self.game_map = game_map

        # self.camera = Camera(self.width, self.height)
        # self.renderer = Renderer(self.screen, tile_size=64)
        self.tile_manager = TileManager()
        
        # Caméra : Permet de déplacer l'affichage sur la carte
        self.camera_x = 0
        self.camera_y = 0
        self.camera_speed = 2  # Vitesse de déplacement de la caméra
        self.viewport_width = 20  # Nombre de tuiles affichées horizontalement
        self.viewport_height = 15  # Nombre de tuiles affichées verticalement

        #  Taille de la carte (en tuiles)
        self.map_size = self.game_map.get_size()
        self.tile_size = 64  # Taille d'une tuile

     
        
    def render_map(self):
        """
        Render only the visible part of the map using the camera.
        """
        town_centre = False

        # 🔹 Chargement de la texture du sol
        grass_block = pygame.transform.scale(pygame.image.load("graphics/block_aoe.png"), (128, 128))

        # 🔹 Dessiner toute la carte avec un décalage caméra
        for x in range(self.map_size):
            for y in range(self.map_size):
                iso_x = (x - self.camera_x) * self.tile_size - (y - self.camera_y) * self.tile_size + self.width // 2
                iso_y = (x - self.camera_x) * (self.tile_size // 2) + (y - self.camera_y) * (self.tile_size // 2) + self.height // 4

                self.screen.blit(grass_block, (iso_x, iso_y))

        # 🔹 Dessiner les objets à leurs positions
        for coordinate, obj in self.game_map.get_map().items():
            x, y = coordinate.get_x(), coordinate.get_y()

            iso_x = (x - self.camera_x) * self.tile_size - (y - self.camera_y) * self.tile_size + self.width // 2
            iso_y = (x - self.camera_x) * (self.tile_size // 2) + (y - self.camera_y) * (self.tile_size // 2) + self.height // 4

            if obj.get_letter() == "T" and not town_centre:
                self.screen.blit(
                    pygame.transform.scale(pygame.image.load("graphics/town_center.png"), (256, 256)),
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

    
    def run(self):
            """
            Main loop for the 2.5D view.
            """
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                # 🔹 Gestion des déplacements de la caméra avec les flèches du clavier
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.camera_x = max(0, self.camera_x - self.camera_speed)
                if keys[pygame.K_RIGHT]:
                    self.camera_x = min(self.map_size - self.viewport_width, self.camera_x + self.camera_speed)
                if keys[pygame.K_UP]:
                    self.camera_y = max(0, self.camera_y - self.camera_speed)
                if keys[pygame.K_DOWN]:
                    self.camera_y = min(self.map_size - self.viewport_height, self.camera_y + self.camera_speed)

                # 🔹 Effacer l'écran et afficher la carte mise à jour
                self.screen.fill((0, 0, 0))
                self.render_map()
                pygame.display.flip()
                self.clock.tick(60)

            pygame.quit()
            