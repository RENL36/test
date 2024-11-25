from model.buildings.building import Building

class TownCenter(Building):
    def __init__(self):
        super().__init__("Town Center", "T", { "W": 350 }, 150, 1000, 4, True)