class Resource:
    def __init__(self, name: str, letter: str, amount: int, spawnable: bool):
        self.name: str = name
        self.letter: str = letter
        self.amount: int = amount
        self.spawnable: bool = spawnable