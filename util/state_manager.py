from enum import Enum

class MapType(Enum):
    """
    Enum representing the different types of maps that can be generated.

    This Enum class defines the various types of maps that can be generated.

    Attributes
    ----------
    RICH : int
        Represents the map type with generous resources dotted across the map.
    GOLD_CENTER : int
        Represents the map type with all the gold at the centre of the map.
    TEST : int
        Represents the map type for testing purposes.
    """
    RICH = 1
    GOLD_CENTER = 2
    TEST = 9

class MapSize(Enum):
    """
    Enum representing the different sizes of the map.

    This Enum class defines the various sizes that the map can be.

    Attributes
    ----------
    SMALL : int
        Represents the small map size of 120x120.
    """
    SMALL = 120

class StartingCondition(Enum):
    """
    Enum representing the different starting conditions of the game.

    This Enum class defines the various starting conditions that the game can be in.

    Attributes
    ----------
    LEAN : int
        Represents the starting condition with lean resources:
            - 50F, 200W, 50G
            - Town Centre, 3 Villagers
    MEAN : int
        Represents the starting condition with mean resources:
            - 2000(F,W,G)
            - Town Centre, 3 Villagers
    MARINES : int
        Represents the starting condition with marines resources:
            - 20000(F,W,G)
            - 3 Town Centres, 15 Villagers, 2 (Barracks, Stable, Archery Range)
    """
    LEAN = 0
    MEAN = 1
    MARINES = 2

class GameState(Enum):
    """
    Enum representing the different states of the game.

    This Enum class defines the various states that the game can be in.

    Attributes
    ----------
    NOT_STARTED : int
        The game has not started yet.
    PLAYING : int
        The game is currently being played.
    PAUSED : int
        The game is currently paused.
    GAME_OVER : int
        The game has ended.
    """
    NOT_STARTED = 0
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3

class FPS(Enum):
    """
    Enum class representing the different frames per second options available in the game.

    This enum class defines the various frames per second options that can be selected from the game's settings.

    Attributes
    ----------
    FPS_15 : int
        Represents the option for 15 frames per second.
    FPS_30 : int
        Represents the option for 30 frames per second.
    FPS_60 : int
        Represents the option for 60 frames per second.
    """
    FPS_15 = 15
    FPS_30 = 30
    FPS_60 = 60

class MenuOptions(Enum):
    """
    Enum class representing the different menu options available in the game.

    This enum class defines the various options that can be selected from the game's menu.

    Attributes
    ----------
    EXIT : int
        Represents the option to exit the game.
    SETTINGS : int
        Represents the option to open the settings menu.
    START_GAME : int
        Represents the option to start a new game.
    RESUME : int
        Represents the option to resume the current game.
    RESTART : int
        Represents the option to restart the current game.
    LOAD_GAME : int
        Represents the option to load a previously saved game.
    SAVE_GAME : int
        Represents the option to save the current game.
    """
    EXIT = 0
    SETTINGS = 1
    START_GAME = 2
    RESUME = 3
    RESTART = 4
    LOAD_GAME = 5
    SAVE_GAME = 6