from model.game_object import GameObject
from util.map import Map


class Render:
    @staticmethod
    def prepare_game_objects(game_map: Map) -> list[GameObject]:
        """
        Prépare la liste des objets de jeu à dessiner dans l'ordre correct pour la vue isométrique.

        :param game_map: La carte contenant les objets.
        :type game_map: Map
        :return: Liste triée des objets à afficher.
        :rtype: list[GameObject]
        """
        objects = []
        for coordinate, obj in game_map.get_map().items():
            if obj:
                objects.append((coordinate, obj))

        # Trier les objets pour respecter l'ordre d'affichage (du haut vers le bas)
        objects.sort(key=lambda item: (item[0].get_y(), item[0].get_x()))
        return objects