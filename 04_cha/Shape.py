import random
import math
from typing import Tuple, List


class _Shape:

    def __init__(self, plane_size: Tuple[int, int, int, int] ):#"minX, minY, maxX, maxY of a plane as a touple"):

        # if (plane_size is not tuple) or len(plane_size) != 4:
        #     raise Exception("Wrong format of a plane size.")
            
        self.plane_size = plane_size
        self.last_vertice = None
        self.choosen_vertice = None
        self.vertices = []

    def get_last_vertice(self) -> Tuple[float, float]:
        return self.last_vertice

    def get_next_vertice(self) -> Tuple[float, float]:
        pass

    def get_random_point_inside(self) -> Tuple[float,float]:
        pass

    def get_all_polygon_vertices(self) -> List[float]:
        result =[]
        if len(self.vertices) != 0:
            for v in self.vertices:
                result.append(v[0])
                result.append(v[1])

        return result

    # def add_vertice(self, pos_x: float, posy_y: float) -> None:
    #     """Add vertice if is within the plane. Otherwise raise an exception"""
    #
    #     if pos_x < self.plane_size[0] or \
    #         posy_y < self.plane_size[1] or \
    #         pos_x > self.plane_size[2] or \
    #         posy_y > self.plane_size[3]:
    #         raise Exception("Given vertice is outside of the plane.")
    #
    #     self.vertices.append(pos_x,posy_y)




class Triangle(_Shape):

    def __init__(self, plane_size: Tuple[int, int, int, int]):
        super().__init__(plane_size)
        triangle_height = self.plane_size[3] - self.plane_size[1]
        triangle_width = self.plane_size[2] - self.plane_size[0]
        if triangle_height < (triangle_width/2) * math.sqrt(3):
            triangle_width = 2 * (triangle_height / math.sqrt(3))
        else:
            triangle_height = (triangle_width / 2) * math.sqrt(3)
        #1st vertice - top
        v1_y = self.plane_size[1]       # Y grows downwards
        v1_x = self.plane_size[2] / 2  # must be in the middle
        #2nd vertice - right corner
        v2_y = triangle_height
        v2_x = triangle_width/2 + v1_x
        #3rd vertice - left corner
        v3_y = v2_y
        v3_x = v2_x - triangle_width

        # self.triangle_height = triangle_height
        # self.triangle_width = triangle_width

        self.vertices.append((v1_x, v1_y))
        self.vertices.append((v2_x, v2_y))
        self.vertices.append((v3_x, v3_y))

    def get_random_point_inside(self) -> Tuple[float,float]:
        # TO DO: return a true random point inside the triangle
        point_y = random.randint( int(self.vertices[0][1]),
                                  int(self.vertices[1][1])
                                  )
        point_x = self.vertices[0][0]
        return (point_x,point_y)

    def get_next_vertice(self) -> Tuple[float,float]:
        """Return a random vertice: (x,y) . Raise Excepcion if there is no vertice added."""

        if len(self.vertices) == 0:
            raise Exception("List of vertices is empty.")
        else:
            self.last_vertice = self.choosen_vertice
            # self.vertice_pool = self.vertices - self.last_vertice
            self.choosen_vertice = random.choice(self.vertices)

        return self.choosen_vertice


class Square(_Shape):

    def __init__(self, plane_size: Tuple[int, int, int, int]):
        super().__init__(plane_size)

    def get_next_vertice(self) -> Tuple[float,float]:
        """Return a random vertice: (x,y) . Raise Excepcion if there is no vertice added."""

        if len(self.vertices) == 0:
            raise Exception("List of vertices is empty.")
        else:
            self.last_vertice = self.choosen_vertice
            self.vertice_pool = self.vertices.remove(self.last_vertice)
            self.choosen_vertice = random.choice(self.vertices)

        return self.choosen_vertice



