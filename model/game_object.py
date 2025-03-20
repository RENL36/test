from util.coordinate import Coordinate

class GameObject:
    object_counter = {}  # Dictionnaire pour suivre le nombre d'instances par type

    def __init__(self, name: str, letter: str, hp: int):
        """
        Initialise un objet de jeu avec un nom unique.

        :param name: Le nom du type d'objet (ex: "Villager", "Soldier").
        :param letter: Lettre représentant l'objet.
        :param hp: Points de vie de l'objet.
        """
        if name not in GameObject.object_counter:
            GameObject.object_counter[name] = 0  # Initialise le compteur

        unique_id = GameObject.object_counter[name]
        GameObject.object_counter[name] += 1  # Incrémente le compteur

        self.__name: str = f"{name}{unique_id}"  # Génère un nom unique (ex: "Villager0")
        self.__letter: str = letter
        self.__hp: int = hp
        self.__coordinate: Coordinate = None
        self.__alive: bool = True
        self.__size: int = 1
        self.__sprite_path: str = None
    
    
    def get_name(self) -> str:
        """
        Returns the name of the object.

        :return: The name of the object.
        :rtype: str
        """
        return self.__name
    
    def get_letter(self) -> str:
        """
        Returns the letter of the object.

        :return: The letter of the object.
        :rtype: str
        """
        return self.__letter
    
    def get_hp(self) -> int:
        """
        Returns the health points of the object.

        :return: The health points of the object.
        :rtype: int
        """
        return self.__hp
    
    def damage(self, damage: int) -> None:
        """
        Inflicts damage to the object.

        :param damage: The amount of damage to inflict.
        :type damage: int
        :raises ValueError: If damage is negative or the entity is already dead.
        """
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        if not self.__alive:
            raise ValueError("Entity is already dead")
        if damage >= self.__hp:
            self.__hp = 0
            self.__alive = False
        else:
            self.__hp -= damage
    
    def get_coordinate(self) -> Coordinate:
        """
        Returns the coordinate of the object.

        :return: The coordinate of the object.
        :rtype: Coordinate
        """
        return self.__coordinate
    
    def set_coordinate(self, coordinate: Coordinate) -> None:
        """
        Sets the coordinate of the object.

        :param coordinate: The new coordinate of the object.
        :type coordinate: Coordinate
        """
        self.__coordinate = coordinate

    def is_alive(self) -> bool:
        """
        Returns True if the object is alive, False otherwise.

        :return: True if the object is alive, False otherwise.
        :rtype: bool
        """
        return self.__alive
    
    def set_alive(self, alive: bool) -> None:
        """
        Sets the alive status of the object.

        :param alive: The new alive status of the object.
        :type alive: bool
        """
        self.__alive = alive

    def get_size(self) -> int:
        """
        Returns the size of the object.

        :return: The size of the object.
        :rtype: int
        """
        return self.__size
    
    def set_size(self, size: int) -> None:
        """
        Sets the size of the object.

        :param size: The new size of the object.
        :type size: int
        """
        self.__size = size

    def get_sprite_path(self) -> str:
        """
        Returns the path to the sprite of the object.

        :return: The path to the sprite of the object.
        :rtype: str
        """
        return self.__sprite_path
    
    def set_sprite_path(self, path: str) -> None:
        """
        Sets the path to the sprite of the object.

        :param path: The new path to the sprite of the object.
        :type path: str
        """
        self.__sprite_path = path

    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        :return: A string representation of the object.
        :rtype: str
        """
        return (f"{self.get_name()} ({self.get_letter()}) - HP : {self.get_hp()}")
