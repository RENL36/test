from model.resources.resource import Resource

class Wood(Resource):
    def __init__(self):
        super().__init__("Wood", "W", 100, True)