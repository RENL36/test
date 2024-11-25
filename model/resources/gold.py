from model.resources.resource import Resource

class Gold(Resource):
    def __init__(self):
        super().__init__("Gold", "G", 800, True)