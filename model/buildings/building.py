from model.maps.coordinate import Coordinate

class Building:
    def __init__(self, name: str, symbol: str, cost: dict, size: tuple, health: int, position: Coordinate, max_health: int, image_path: str):
        """
        Classe de base pour tous les bâtiments.
        :param name: Nom du bâtiment.
        :param symbol: Symbole du bâtiment pour la vue terminale.
        :param cost: Coût de construction (dict avec types de ressources).
        :param size: Taille (tuple représentant largeur et hauteur).
        :param health: Points de vie.
        :param position: Coordonnées sur la carte.
        :param max_health : santé maximale du batiment
        :param image_path : chemin de l'image associée
        """
        self.name: str = name
        self.symbol: str = symbol
        self.cost: dict = cost
        self.size: int = size
        self.health: int = health
        self.position: Coordinate = position
        self.max_health: int = max_health
        self.image_path: str = image_path

    def __str__(self) -> str:
        return f"{self.name} ({self.symbol}) à {self.position} - Santé: {self.health}"

    def take_damage(self, amount: int) -> None:
        """Réduit les points de vie du bâtiment."""
        self.health -= amount
        if self.health <= 0:
            self.health = 0

    def is_destroyed(self) -> bool:
        """Vérifie si le bâtiment est détruit."""
        return self.health <= 0

    def get_position(self) -> Coordinate:
        """Retourne les coordonnées actuelles du bâtiment """
        return self.position