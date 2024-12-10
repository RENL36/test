from model.maps.coordinate import Coordinate
from model.buildings.town_center import TownCenter
from model.buildings.barracks import Barracks

def main():
    # Création d'une position pour le TownCenter et la Barracks
    town_center_position = Coordinate(x=5, y=5)
    barracks_position = Coordinate(x=10, y=10)

    # Initialisation du TownCenter
    town_center = TownCenter(position=town_center_position)
    assert town_center.name == "Town Center"
    assert town_center.symbol == "T"

    # Initialisation de la Barracks
    barracks = Barracks(position=barracks_position)
    assert barracks.name == "Barracks"
    assert barracks.symbol == "B"

    # Test : Dégâts infligés au TownCenter
    town_center.take_damage(300)
    assert town_center.health == 700

    # Test : Dégâts suffisants pour détruire la Barracks
    barracks.take_damage(1000)
    assert barracks.is_destroyed

    # Test : Position des bâtiments
    assert town_center.get_position() == town_center_position
    assert barracks.get_position() == barracks_position

if __name__ == "__main__":
    main()