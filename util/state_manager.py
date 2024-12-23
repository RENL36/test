from enum import Enum

"""
Define the different types of maps that can be generated:
    - RICH : Generous resources dotted across the map
    - GOLD_CENTER : All the gold is at the centre of the map
    - TEST : For testing purposes
"""
class MapType(Enum):
    RICH = 1
    GOLD_CENTER = 2
    TEST = 9

"""
Define the size of the map:
    - SMALL : 120x120
"""
class MapSize(Enum):
    SMALL = 0

"""
Define the ressources allocated to each player at the beginning of the game:
    - LEAN :
        - 50F, 200W, 50G
        - Town Centre, 3 Villagers
    - MEAN :
        - 2000(F,W,G)
        - Town Centre, 3 Villagers
    - MARINES :
        - 20000(F,W,G)
        - 3 Town Centres, 15 Villagers, 2 (Barracks, Stable, Archery Range)
"""
class StartingCondition(Enum):
    LEAN = 0
    MEAN = 1
    MARINES = 2

"""
Define the different states of the game:
    - NOT_STARTED : The game has not started yet
    - PLAY : The game is currently being played
    - PAUSE : The game is paused
    - GAME_OVER : The game is finished
"""
class GameState(Enum):
    NOT_STARTED = 0
    PLAY = 1
    PAUSE = 2
    GAME_OVER = 3

"""
Define the FPS options available:
    - FPS_15 : 15 FPS
    - FPS_30 : 30 FPS
    - FPS_60 : 60 FPS
"""
class FPS(Enum):
    FPS_15 = 15
    FPS_30 = 30
    FPS_60 = 60

"""
Define the different options available in the menu:
    - EXIT : Exit the game
    - SETTINGS : Open the settings menu
    - START_GAME : Start a new game
    - LOAD_GAME : Load a saved game
    - RESUME : Resume the game
    - RESTART : Restart the game
    - SAVE_GAME : Save the game
"""
class MenuOptions(Enum):
    EXIT = 0
    SETTINGS = 1
    START_GAME = 2
    RESUME = 3
    RESTART = 4
    LOAD_GAME = 5
    SAVE_GAME = 6