from model.resources.resource import Resource

class Food(Resource):
    def __init__(self):
        super().__init__("Food", "F", 300, False)