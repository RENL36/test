from util.map import Map
from model.player.player import Player
from model.game_object import GameObject
from model.units.unit import Unit
from util.coordinate import Coordinate
from model.resources.resource import Resource
from model.units.villager import Villager
from model.buildings.building import Building
from model.entity import Entity


class Interactions:
    def __init__(self, map: Map) -> None:
        self.__map: Map = map
    
    def place_object(self, object: GameObject, coordinate: Coordinate) -> None:
        """
        Place an object on the map, at a certain coordinate. 
        :param object: The object to place on the map.
        :type object: GameObject
        :param coordinate: The coordinate where to place the object.
        :type coordinate: Coordinate
        """
        self.__map.add(object, coordinate)
        object.set_coordinate(coordinate)
    
    def remove_object(self, object: GameObject) -> None:
        """
        Remove an object from the map.
        :param object: The object to remove from the map.
        :type object: GameObject
        """
        self.__map.remove(object.get_coordinate())
        object.set_coordinate(None)
        object.set_alive(False)
    
    def move_unit(self, unit: Unit, coordinate: Coordinate) -> None:
        """
        Move a unit to a certain coordinate.
        :param unit: The unit to move.
        :type unit: Unit
        :param coordinate: The coordinate where to move the unit.
        :type coordinate: Coordinate
        """
        self.__map.move(unit, coordinate)
        unit.set_coordinate(coordinate)
    
    def attack(self, attacker: Unit, target_coord: Coordinate) -> None:
        """
        Attack
        :param attacker: The unit that attacks.
        :type attacker: Unit
        :param target_coord: The coordinate of the target.
        :type target_coord: Coordinate
        """
        if attacker.get_coordinate().distance(target_coord) > attacker.get_range():
            raise ValueError("Target is out of range.")
        target: GameObject = self.__map.get(target_coord)
        if target is None:
            raise ValueError("No target found at the given coordinate.")
        if isinstance(target,Resource):
            raise ValueError("Target is a resource.")
        target.damage(attacker.get_attack_per_second()) # Damage the target

        if not target.is_alive():
            self.remove_object(target) # Remove the target from the map
        if isinstance(target, Building) and target.is_population_increase():
            owner = target.get_player()
            owner.set_max_population(owner.get_max_population() - target.get_capacity_increase())
    
    def collect_resource(self, villager: Villager, resource_coord: Coordinate, amount: int) -> None:
        """
        Collect a resource.
        :param villager: The villager that collects the resource.
        :type villager: Villager
        :param resource_coord: The coordinate of the resource.
        :type resource_coord: Coordinate
        :param amount: The amount of resource to collect.
        :type amount: int
        """
        if not villager.get_coordinate().is_adjacent(resource_coord):
            raise ValueError("Resource is out of range.")
        resource: GameObject = self.__map.get(resource_coord)
        if resource is None:
            raise ValueError("No resource found at the given coordinate.")
        if not isinstance(resource,Resource):
            raise ValueError("Target is not a resource.")
        
        amount = resource.collect(amount) # Collect the resource
        villager.stock_resource(resource)
        if not resource.is_alive():
            self.remove_object(resource) # Remove the resource from the map
    
    def drop_resource(self, player: Player, villager: Villager, target_coord: Coordinate) -> None:
        """
        Drop the resources to a drop point.
        :param player: The player that owns the villager.
        :type player: Player
        :param villager: The villager that drops the resources.
        :type villager: Villager
        :param target_coord: The coordinate of the drop point.
        :type target_coord: Coordinate
        """
        if not villager.get_coordinate().is_adjacent(target_coord):
            raise ValueError("Target is out of range.")
        target: GameObject = self.__map.get(target_coord)
        if target is None:
            raise ValueError("No target found at the given coordinate.")
        if not isinstance(target, Building):
            raise ValueError("Target is not a building.")
        if not target.is_resources_drop_point():
            raise ValueError("Target is not a resource drop point.")
        
        for resource, amount in villager.empty_resource().items():
            player.collect(resource, amount)
    def link_owner(self, player: Player, entity: Entity) -> None:
        """
        Link an owner to an entity.
        :param player: The player that owns the entity.
        :type player: Player
        :param entity: The entity that is owned.
        :type entity: Entity
        """
        entity.set_player(player)
        if isinstance(entity, Building):
            player.add_building(entity)
        if isinstance(entity, Unit):
            player.add_unit(entity)