import pygame

class TileManager:
    """
    Classe pour gérer les textures des tuiles.
    """

    def __init__(self):
        """
        Initialise le gestionnaire de tuiles.
        """
        self.textures = {
            # "grass": pygame.transform.scale(pygame.image.load("graphics/grass.png"), (64, 64)),
            # "water": pygame.transform.scale(pygame.image.load("graphics/water.png"), (64, 64)),
            "town_center": pygame.transform.scale(pygame.image.load("graphics/town_center.png"), (64, 64)),
            "villager": pygame.transform.scale(pygame.image.load("graphics/villager.png"), (48, 48)),
            # "grass_tiles": pygame.transform.scale(pygame.image.load("assets/terrain/grass11.png"), (800, 600)),
            "wood": pygame.transform.scale(pygame.image.load("graphics/tree.png"), (64, 64)),
            "food": pygame.image.load("graphics/farm_2.png"),
            "gold": pygame.transform.scale(pygame.image.load("graphics/gold.png"), (64, 64)),
            "swordsman": pygame.transform.scale(pygame.image.load("graphics/pikeman.png"), (48, 48)),
            "horseman": pygame.transform.scale(pygame.image.load("graphics/cavalier.png"), (64, 64)),
            "archer": pygame.transform.scale(pygame.image.load("graphics/archer.png"), (64, 64)),
            "house": pygame.transform.scale(pygame.image.load("graphics/house.png"), (64, 64)),
            "camp": pygame.transform.scale(pygame.image.load("graphics/camp.png"), (64, 64)),
            "barracks": pygame.transform.scale(pygame.image.load("graphics/secondage_barracks.png"), (64, 64)),
            "stable": pygame.transform.scale(pygame.image.load("graphics/stable.png"), (64, 64)),
            "archery_range": pygame.transform.scale(pygame.image.load("graphics/secondage_archery.png"), (64, 64)),
            "keep": pygame.transform.scale(pygame.image.load("graphics/keep.png"), (64, 64))
        }

    def get_texture(self, texture_name):
        """
        Retourne la texture demandée.

        :param texture_name: Nom de la texture.
        :return: L'image de la texture.
        """
        return self.textures.get(texture_name, None)