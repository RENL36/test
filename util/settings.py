from util.state_manager import FPS, MapSize, MapType, StartingCondition

class Settings:
    """
    A class to represent the game settings.

    This class is used to store the game settings and allows the user to change them.

    Attributes
    ----------
    map_type : MapType
        The type of the map (default is MapType.RICH).
    map_size : MapSize
        The size of the map (default is MapSize.SMALL).
    starting_condition : StartingCondition
        The starting condition of the game (default is StartingCondition.LEAN).
    fps : int
        The frames per second setting (default is FPS.FPS_60).

    Methods
    -------
    __init__():
        Initializes the Settings object with default values.
    """
    def __init__(self) -> None:
        """Create a new Settings object with default values. It is used to store the game settings and allows the user to change them."""
        self.map_type: MapType = MapType.RICH
        self.map_size: MapSize = MapSize.SMALL
        self.starting_condition: StartingCondition = StartingCondition.LEAN
        self.fps: int = FPS.FPS_60