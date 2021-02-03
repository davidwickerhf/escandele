from typing import List, Literal, Tuple, Union, TYPE_CHECKING
if TYPE_CHECKING:
    from escandele.light import LightSpot


class Spot:
    """A Spot in the room.

    Args:
        x (int): x coordinate of the spot
        y (int): y coordinate of the spot


    Attributes:
        x (int): x coordinate of the spot
        y (int): y coordinate of the spot
        light (int): Strengh of the light that reaches this spot.
    """
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.light = 0

    def __repr__(self) -> str:
        return f'<Spot: {self.x}, {self.y} | {self.light}>'

    def distance(self, spot:'Spot'):
        """Distance between two spots.

        If the two spots share the same x axis, then the
        distance will be defined by the absolute value of the
        difference in the y axis.

        If the two spots share the same y axis, then the 
        distance will be defined by the absolute value of the 
        difference in the x axis.

        If both x and y axis are different, then the distance
        will be defined by the greatest value of the
        difference between x axisses and y axxises.

        Args:
            spot (Spot): The spot to calculate the distance from.

        Returns:
            int: Distance between the spots.
        """
        if self.x == spot.x:
            return abs(self.y - spot.y)
        elif self.y == spot.y:
            return abs(self.x - spot.x)

        dxx = abs(self.x - spot.x)
        dyy = abs(self.y - spot.y)
        return max(dxx, dyy)


    def assign_light(self, lights: List['LightSpot']):
        """Determine the light that reaches this spot

        The light that reaches the spot is determined based on
        the light spots that are given in the arguments.
        If multiple light pooints have influence on a spot in the room,
        the spot's light will be determined by the strongest light point.

        This method will assign this :class:`Spot` instance's ``light`` parameter.

        Args:
            lights (List[:class:`LightSpot`]): [description]

        Returns:
            :class:`Spot`: Returns the spot, with the newly assigned light strengh.
        
        """
        # Define recevied light for every source
        received:List[int] = list()
        for light in lights:
            # Define distance from light
            rlight = light.light
            distance = self.distance(light)
            for d in range(distance):
                if rlight > 0:
                    rlight -= 1
            received.append(rlight)

        self.light = max(received)
        return self

    def is_dark(self):
        return self.light == 0