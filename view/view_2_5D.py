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

    def render_map(self):
        """
        Render the map with objects and textures.
        """
        town_centre = False

        # displaying the ground blocks in an isometric way
        grass_block = pygame.transform.scale(pygame.image.load("graphics/block_aoe.png"), (128, 128))
        for x in range(10):
            for y in range(10):
                self.screen.blit(grass_block, (700 + x*64 - y*64, 100 + x*32 + y*32))

        # display the grass background
        # self.screen.blit(self.tile_manager.get_texture("grass_tiles"), (0, 0))
        # self.screen.blit(self.tile_manager.get_texture("grass_tiles"), (640, 0))

        # iterating through all of the objects in order to display them
        for coordinate, obj in self.game_map.get_map().items():
            # initialising the coordinates of the object on the map
            x, y = coordinate.get_x(), coordinate.get_y()
            texture = None

            if obj:
                if obj.get_letter() == "T":
                    # texture = self.tile_manager.get_texture("town_center")
                    # self.renderer.render_tile(x+2, y, texture, self.camera)
                    # self.renderer.render_tile(x, y+2, texture, self.camera)
                    # self.renderer.render_tile(x+2, y+2, texture, self.camera)

                    if not town_centre:
                        self.screen.blit(pygame.transform.scale(pygame.image.load("graphics/town_center.png"), (256, 256)), (630 + x*64 - y*64, 50 + 32*x + 32*y))
                        # self.screen.blit(pygame.transform.scale(pygame.image.load("graphics/town_center.png"), (32*4, 32*4)), (720 + 64*(x+2) - y*64, 70 + 32*(x+2) + 32*y))
                        # self.screen.blit(pygame.transform.scale(pygame.image.load("graphics/town_center.png"), (32*4, 32*4)), (720 + 64*x - 64*(y+2), 70 + 32*x + 32*(y+2)))
                        # self.screen.blit(pygame.transform.scale(pygame.image.load("graphics/town_center.png"), (32*4, 32*4)), (720 + 64*(x+2) - 64*(y+2),70 + 32*(x+2) +32*(y+2)))
                        town_centre = True

                elif obj.get_letter() == "v":
                    self.screen.blit(self.tile_manager.get_texture('villager'), (740 + 64*x - 64*y, 90 + 32*x + 32*y))

                elif obj.get_letter() == "s":
                    self.screen.blit(self.tile_manager.get_texture('swordsman'), (740 + 64*x - 64*y, 90 + 32*x + 32*y))

                elif obj.get_letter() == "h":
                    self.screen.blit(self.tile_manager.get_texture('horseman'), (730 + 64*x - 64*y, 85 + 32*x + 32*y))

                elif obj.get_letter() == "a":
                    self.screen.blit(self.tile_manager.get_texture('archer'), (725 + 64*x - 64*y, 80 + 32*x + 32*y))

                elif obj.get_letter() == "H":
                    self.screen.blit(self.tile_manager.get_texture("house"), (735 + 64*x - 64*y, 85 + 32*x + 32*y))

                elif obj.get_letter() == "C":
                    self.screen.blit(self.tile_manager.get_texture("camp"), (730 + 64*x - 64*y, 95 + 32*x + 32*y))

                elif obj.get_letter() == "B":
                    self.screen.blit(self.tile_manager.get_texture("barracks"), (735 + 64*x - 64*y, 90 + 32*x + 32*y))

                elif obj.get_letter() == "S":
                    self.screen.blit(self.tile_manager.get_texture("stable"), (735 + 64*x - 64*y, 90 + 32*x + 32*y))

                elif obj.get_letter() == "A":
                    self.screen.blit(self.tile_manager.get_texture("archery_range"), (735 + 64*x - 64*y, 90 + 32*x + 32*y))

                elif obj.get_letter() == "K":
                    self.screen.blit(self.tile_manager.get_texture("keep"), (725 + 64*x - 64*y, 85 + 32*x + 32*y))

                elif obj.get_letter() == "W":
                    self.screen.blit(self.tile_manager.get_texture("wood"), (740 + 64*x - 64*y, 85 + 32*x + 32*y))

                elif obj.get_letter() == "F":
                    self.screen.blit(self.tile_manager.get_texture("food"), (710 + 64*x - 64*y, 102 + 32*x + 32*y))

                elif obj.get_letter() == "G":
                    self.screen.blit(self.tile_manager.get_texture("gold"), (730 + 64*x - 64*y, 95 + 32*x + 32*y))

            
            # self.renderer.render_tile(x, y, texture, self.camera)

    
    def run(self):
        """
        Main loop for the 2.5D view.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear the screen
            self.screen.fill((0, 0, 0))

            # self.renderer.render_tile(100, 100, self.tile_manager.get_texture("town_center"), self.camera)
            

            # Render the map
            self.render_map()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

      