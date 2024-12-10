from model.maps.coordinate import Coordinate

class Building:
    def __init__(self, name, symbol, cost, size, health, position:Coordinate,max_health):
        """
        Classe de base pour tous les bâtiments.
        :param name: Nom du bâtiment.
        :param symbol: Symbole du bâtiment pour la vue terminale.
        :param cost: Coût de construction (dict avec types de ressources).
        :param size: Taille (tuple représentant largeur et hauteur).
        :param health: Points de vie.
        :param position: Coordonnées sur la carte.
        :param max_health : santé maximale du batiment
        """
        self.name = name
        self.symbol = symbol
        self.cost = cost
        self.size = size
        self.health = health
        self.position = position
        self.max_health=max_health

    def __str__(self):
        return f"{self.name} ({self.symbol}) à {self.position} - Santé: {self.health}"

    def take_damage(self, amount):
        """Réduit les points de vie du bâtiment."""
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} a été détruit.")
            self.health = 0
    def repair(self,amount:int):
        """ 
        Répare le bâtiment en augmentant ses PV, jusqu’à sa santé maximale.
        """
        self.health=min(self.health+amount ,self.max_health)
    def is_destroyed(self)-> bool:
        """ Vérifie si le bâtiment est détruit."""
        return self.health<=0
    def get_position(self) -> Coordinate:
        """Retourne les coordonnées actuelles du bâtiment """
        return self.position
        