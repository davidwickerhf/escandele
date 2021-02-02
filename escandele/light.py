from escandele.spot import Spot



class LightSpot(Spot):
    """A Spot in the room.

    Args:
        x (int): x coordinate of the spot
        y (int): y coordinate of the spot
        strenght (int): Strengh of the light.
    """
    def __init__(self, x, y, strenght) -> None:
        super().__init__(x, y)
        self.light  = strenght

    def assign_light(self):
        pass