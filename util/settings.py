from util.state_manager import FPS, MapSize, MapType, StartingCondition

class Settings:
    def __init__(self) -> None:
        """Create a new Settings object with default values. It is used to store the game settings and allows the user to change them."""
        self.map_type: MapType = MapType.RICH
        self.map_size: MapSize = MapSize.SMALL
        self.starting_condition: StartingCondition = StartingCondition.LEAN
        self.fps: int = FPS.FPS_60