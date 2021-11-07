import random
from typing import Tuple

class _Shape:



    def __init__(self, plane_size: "minX, minY, maxX, maxY of a plane as a touple"):

        if not(plane_size is Tuple) or len(plane_size) != 4:
            raise Exception("Wrong format of a plane size.")
            
        self.plane_size = plane_size
        self.last_vertice = None
        self.choosen_vertice = None
        self.vertices = {}


    def add_vertice(self, pos_x: float, posy_y: float) -> None:
        """Add vertice if is within the plane. Otherwise raise an exception"""

        if pos_x < self.plane_size[0] or posy_y < self.plane_size[1] or pos_x > self.plane_size[2] or posy_y > self.plane_size[3]:
            raise Exception("Given vertice is outside of the plane.")

        self.vertices.add(pos_x,posy_y)


    def get_vertice(self) -> Tuple[float,float]:
        """Return a random vertice: (x,y) . Raise Excepcion if there is no vertice added."""

        if len(self.vertices) == 0:
            raise Exception("List of vertices is empty.")
        else:
            self.last_vertice = self.choosen_vertice
            self.vertice_pool = self.vertices.remove(self.last_vertice)
            self.choosen_vertice = random.choice(self.vertices)

        return self.choosen_vertice


