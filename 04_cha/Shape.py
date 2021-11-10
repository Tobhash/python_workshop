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

    def get_next_vertice(self) -> Tuple[float, float]:
        """Return a random vertice: (x,y) . Raise Excepcion if there is no vertice added."""

        if len(self.vertices) == 0:
            raise Exception("List of vertices is empty.")
        else:
            # =====
            # Variant 0:
            # choose random vertex
            # =====
            self.last_vertice = self.choosen_vertice
            self.choosen_vertice = random.choice(self.vertices)

        return self.choosen_vertice

    def get_all_polygon_vertices(self) -> List[float]:
        result =[]
        if len(self.vertices) != 0:
            for v in self.vertices:
                result.append(int(v[0]))
                result.append(int(v[1]))

        return result

    def get_last_vertice(self) -> Tuple[float, float]:
        return self.last_vertice

    def get_random_point_inside(self) -> Tuple[float,float]:
        pass



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

    # def get_next_vertice(self) -> Tuple[float,float]:
    #     """Return a random vertice: (x,y) . Raise Excepcion if there is no vertice added."""
    #
    #     if len(self.vertices) == 0:
    #         raise Exception("List of vertices is empty.")
    #     else:
    #         self.last_vertice = self.choosen_vertice
    #         # self.vertice_pool = self.vertices - self.last_vertice
    #         self.choosen_vertice = random.choice(self.vertices)
    #
    #     return self.choosen_vertice


class Square(_Shape):

    def __init__(self, plane_size: Tuple[int, int, int, int]):
        super().__init__(plane_size)

        square_width = self.plane_size[2] - self.plane_size[0]
        square_height = self.plane_size[3] - self.plane_size[1]

        square_side_length = square_width if square_width < square_height else square_height

        #1st vertice(top left)
        pad_y = (square_height - square_side_length) / 2
        pad_x = (square_width - square_side_length) / 2
        v1_x = self.plane_size[0] + pad_x
        v1_y = self.plane_size[1] + pad_y
        v1 = (v1_x, v1_y)

        #2nd vertice(top right)
        v2 = (v1[0] + square_side_length, v1[1])

        #3rd vertice(bottom righ)
        v3 = (v2[0], v2[1] + square_side_length)

        #4th vertice(bottom left)
        v4 = (v1[0], v3[1])

        self.vertices.append(v1)
        self.vertices.append(v2)
        self.vertices.append(v3)
        self.vertices.append(v4)

        self.choosen_vertice = random.choice(self.vertices)
        # used to randomly choice next vertices
        self.indexes = [0, 1, 2, 3]


    def get_random_point_inside(self) -> Tuple[float,float]:
        # choice( v1_x + 1, v2_x - 1)
        point_x = random.randint(int(self.vertices[0][0] + 1),
                                 int(self.vertices[1][0] - 1)
                                 )
        # choice( v1_y + 1, v3_y - 1)
        point_y = random.randint(int(self.vertices[0][1] + 1),
                                 int(self.vertices[3][1] - 1)
                                 )
        return (point_x, point_y)

    def get_next_vertice(self) -> Tuple[float,float]:
        """Return a random vertice: (x,y) . Raise Excepcion if there is no vertice added."""
        if len(self.vertices) == 0:
            raise Exception("List of vertices is empty.")
        else:
            # =====
            # Variant 1:
            # the current vertex cannot be chosen in the next iteration
            # &
            # the current vertex cannot be one place away(anti - clockwise) from the previously chosen vertex
            # =====
            self.last_vertice = self.choosen_vertice
            restriction_index_1 = self.vertices.index(self.last_vertice)
            restriction_index_2 = (restriction_index_1 - 1) % len(self.vertices)

            self.indexes.remove(restriction_index_1)
            self.indexes.remove(restriction_index_2)
            self.choosen_vertice = self.vertices[random.choice(self.indexes)]
            self.indexes = [0, 1, 2, 3]

            # self.vertice_pool = self.vertices - [ self.vertices[restriction_index] ]
            # self.choosen_vertice = random.choice(self.vertice_pool)

        return self.choosen_vertice


class Pentagon(_Shape):
    def __init__(self, plane_size: Tuple[int, int, int, int]):
        super().__init__(plane_size)

        plane_width = self.plane_size[2] - self.plane_size[0]
        plane_height = self.plane_size[3] - self.plane_size[1]

        gamma = 0.5527864       # Pentagon HEIGHT to circle radius ratio
        # radius = (plane_height if plane_height < plane_width else plane_width) / 2
        H = (plane_height if plane_height < plane_width else plane_width)
        radius = round(H * gamma, 2)

        center = (plane_width / 2, radius)
        side_lenght = 2 * (radius * math.cos(math.radians(54)))

        # 1st vertex (top)
        v1_x = center[0]
        v1_y = center[1] - radius

        v1_x = round(v1_x, 0)
        v1_y = round(v1_y, 0)

        # 2nd vertex (middle-right)
        v2_x = v1_x + side_lenght * math.cos(math.radians(36))
        v2_y = v1_y + side_lenght * math.sin(math.radians(36))

        v2_x = round(v2_x, 0)
        v2_y = round(v2_y, 0)

        # 3rd vertex (bottom-right)
        v3_x = v2_x - side_lenght * math.sin(math.radians(18))
        v3_y = v2_y + side_lenght * math.cos(math.radians(18))

        v3_x = round(v3_x, 0)
        v3_y = round(v3_y, 0)

        # 5th vertex (middle-left)
        v5_x = v1_x - side_lenght * math.cos(math.radians(36))
        v5_y = v2_y

        v5_x = round(v5_x, 0)
        v5_y = round(v5_y, 0)

        # 4th vertex (bottom-left)
        v4_x = v5_x + side_lenght * math.sin(math.radians(18))
        v4_y = v3_y

        v4_x = round(v4_x, 0)
        v4_y = round(v4_y, 0)



        self.vertices.append((v1_x, v1_y))
        self.vertices.append((v2_x, v2_y))
        self.vertices.append((v3_x, v3_y))
        self.vertices.append((v4_x, v4_y))
        self.vertices.append((v5_x, v5_y))

        self.choosen_vertice = random.choice(self.vertices)
        self.radius = radius
        self.center = center
        self. indexes = [0, 1, 2, 3, 4]
        self.last_index = 1
        self.last_last_index = 0

    def get_random_point_inside(self) -> Tuple[float, float]:
        inner_radius = self.radius * math.sin(math.radians(54))
        angle = math.radians(random.randint(0, 180))
        point_x = self.center[0] + inner_radius * math.cos(angle)
        point_y = self.center[1] + inner_radius * math.sin(angle)

        return point_x, point_y

    def get_next_vertice(self) -> Tuple[float, float]:
        """Return a random vertice: (x,y) . Raise Excepcion if there is no vertice added."""
        # super().get_next_vertice()


        if len(self.vertices) == 0:
            raise Exception("List of vertices is empty.")
        else:
            # =====
            # Variant 1:
            # the currently chosen vertex cannot neighbor the previously chosen vertex
            # if the two previously chosen vertices are the same.
            # =====

            chosen_index = None
            if self.last_last_index == self.last_index:
                restricted_index1 = self.last_index
                restricted_index2 = (restricted_index1 + 1) % len(self.indexes)
                restricted_index3 = (restricted_index1 - 1) % len(self.indexes)

                self.indexes.remove(restricted_index1)
                self.indexes.remove(restricted_index2)
                self.indexes.remove(restricted_index3)

                chosen_index = random.choice(self.indexes)
                self.indexes = [0, 1, 2, 3, 4]
            else:
                chosen_index = random.choice(self.indexes)

            self.choosen_vertice = self.vertices[chosen_index]

            self.last_last_index = self.last_index
            self.last_index = chosen_index

            # # ====
            # # Variant 2
            # # ====
            #
            # self.indexes.remove(self.last_index)
            # index = random.choice(self.indexes)
            # self.choosen_vertice = self.vertices[index]
            # self.indexes = [0, 1, 2, 3, 4]
            # self.last_index = index

        return self.choosen_vertice








