from typing import List, Literal, Tuple, Union
from escandele import Spot, LightSpot




class Room:
    """Class to reppresent room objects.

    Args:
        room (List[List[Literal['x', 'c']]]): Matrix reppresentation of the room.
        l (int): Strenght of the light sources.

    Attributes:
        spots (List[Spot]): List of the empty spots in the room
        lights (List[Lights]): List of the light sources in the room.
        n (int): Size of the room
        l (int): Strengh of the light sources.

    """
    def __init__(self, room:List[List[Literal['x', 'c']]], l:int) -> None:
        self.spots:List[Spot] = list()
        self.lights:List[LightSpot] = list()
        self.n = len(room)
        self.l = l

        # Map the room matrix into a room object
        for y, xline in enumerate(room):
            if len(xline) != self.n:
                raise ValueError(xline)
            for x, value in enumerate(xline):
                if value in ('c', 'C'):
                    spot = LightSpot(x, y, l)
                    self.lights.append(spot)
                    continue
                spot = Spot(x, y)
                self.spots.append(spot)

        self.calculate_light()

    def __repr__(self) -> str:
        return f'<Room: {self.n}>'

    
    def calculate_light(self):
        """Calculate the light received by each empty 
        spot in the room.
        """
        for spot in self.spots:
            spot.assign_light(self.lights)   


    @property
    def empty_spots(self):
        spots = list()
        for spot in self.spots:
            if spot.is_dark():
                spots.append(spot)
        return spots

    
    @staticmethod
    def empty_room(n:int):
        """Generate an empty room matrix with a size of n

        Args:
            n (int): Size of the matrix.

        Returns:
            List[List]: Empty Matrix
        """
        room = list()
        for y in range(n):
            xlist = list()
            for x in range(n):
                xlist.append(0)
            room.append(xlist)
        return room


    @property
    def light_matrix(self):
        """Matrix reppresentation of the room,
        with calculated lights spots.

        Returns:
            List[List[int]]: matrix
        """
        # Generate Empty Matrix
        room = self.empty_room(self.n)
        
        for spot in self.spots:
            room[spot.x][spot.y] = spot.light

        for spot in self.lights:
            room[spot.x][spot.y] = spot.light
        
        return room


    @property
    def original_matrix(self):
        """Matrix reppresentation of the original room.

        Returns:
            List[List[Literal['x', 'c']]]: matrix
        """
        # Generate Empty Matrix
        room = self.empty_room(self.n)
        
        for spot in self.spots:
            room[spot.x][spot.y] = 'x'

        for spot in self.lights:
            room[spot.x][spot.y] = 'c'
        
        return room                    


    @classmethod
    def from_coords(cls, n:int, l:int, lights:Union[Tuple[int, int], List[Tuple[int, int]]]):
        """Generate a room object.

        Create a room object by it's lenght and coordinates of any light points.

        Args:
            n (int): Size of the room
            l (int): Strenght of the light points
            lights (Union[Tuple[int, int], List[Tuple[int, int]]]): List 
                of coordinates of the various light points (x, y)
            

        Returns:
            [type]: [description]
        """
        for coord in lights:
            if len(coord) > 2 or len(coord) < 2:
                raise ValueError(coord)
            elif coord[0] not in range(0, n):
                raise ValueError(coord)
            elif coord[1] not in range(0, n):
                raise ValueError(coord)
            
        matrix:List[List] = cls.empty_room(n)

        if isinstance(lights, tuple):
            lights = [lights]

        for x, xlist in enumerate(matrix):
            for y, value in enumerate(xlist):
                coord = (x, y)
                if coord in lights:
                    matrix[x][y] = 'c'
                    continue
                matrix[x][y] = 'x'

        return cls(room=matrix, l=l)  