import pygame
from util.coordinate import Coordinate
from util.map import Map
from model.game_object import GameObject


class View2D5:
    def __init__(self, game_map: Map, screen_width: int = 800, screen_height: int = 600):
        """
        Initialise la vue 2.5D.

        :param game_map: L'objet Map contenant les données de la carte.
        :type game_map: Map
        :param screen_width: Largeur de la fenêtre.
        :type screen_width: int
        :param screen_height: Hauteur de la fenêtre.
        :type screen_height: int
        """
        print(f"Initializing View2D5 with width={screen_width}, height={screen_height}")
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("2.5D View")
        self.clock = pygame.time.Clock()
        self.map = game_map
        self.tile_size = 64  # Taille des tuiles en pixels
        self.offset_x = screen_width // 2
        self.offset_y = 50

    def __convert_to_isometric(self, x: int, y: int) -> tuple[int, int]:
        """
        Convertit des coordonnées cartésiennes en coordonnées isométriques.

        :param x: Coordonnée x en cartésien.
        :type x: int
        :param y: Coordonnée y en cartésien.
        :type y: int
        :return: Coordonnées isométriques.
        :rtype: tuple[int, int]
        """
        iso_x = (x - y) * (self.tile_size // 2)
        iso_y = (x + y) * (self.tile_size // 4)
        return iso_x + self.offset_x, iso_y + self.offset_y

    def render(self) -> None:
        """
        Rendu de la vue 2.5D.
        """
        self.screen.fill((0, 0, 0))  # Fond noir
        for y in range(self.map.get_size()):
            for x in range(self.map.get_size()):
                coord = Coordinate(x, y)
                obj = self.map.get(coord)
                iso_x, iso_y = self.__convert_to_isometric(x, y)

                # Dessine les tuiles de terrain
                pygame.draw.polygon(
                    self.screen,
                    (50, 150, 50),
                    [
                        (iso_x, iso_y + self.tile_size // 4),
                        (iso_x + self.tile_size // 2, iso_y),
                        (iso_x + self.tile_size, iso_y + self.tile_size // 4),
                        (iso_x + self.tile_size // 2, iso_y + self.tile_size // 2),
                    ],
                )

                # Dessine les objets
                if obj:
                    sprite_path = obj.get_sprite_path()
                    if sprite_path:
                        sprite = pygame.image.load(sprite_path).convert_alpha()
                        sprite = pygame.transform.scale(sprite, (self.tile_size, self.tile_size))
                        self.screen.blit(sprite, (iso_x, iso_y - self.tile_size // 2))
    def exit(self):
        """Stop the 2.5D view."""
        self.running = False  # Stop the loop

    def show(self) -> None:
        """
        Affiche la vue 2.5D.
        """
        if not pygame.get_init():
             pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.render()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()