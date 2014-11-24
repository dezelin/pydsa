
import unittest


class Vertex(object):
    """ Graph vertex implementation """

    def __init__(self, id):
        self.__id = id
        self.__neighbors = {}

    def add_neighbor(self, v, cost=0):
        self.__neighbors[v] = cost

    def get_connections(self):
        return self.__neighbors.keys()

    def get_id(self):
        return self.__id

    def get_weight(self, v):
        return self.__neighbors[v]


class Graph(object):
    """ Graph implementation """

    def __init__(self):
        self.__size = 0
        self.__vertices = {}

    def add_vertex(self, key):
        if key in self.__vertices:
            return

        v = Vertex(key)
        self.__vertices[key] = v
        self.__size += 1
        return v

    def add_edge(self, key0, key1, cost=0):
        if key0 not in self.__vertices:
            self.add_vertex(key0)

        if key1 not in self.__vertices:
            self.add_vertex(key1)

        self.__vertices[key0].add_neighbor(key1, cost)

    def get_vertices(self):
        return self.__vertices.keys()


class TestVertex(unittest.TestCase):
    """ Test case for Vertex class """

    def test__init__(self):
        v = Vertex(12345)
        assert v.get_id() == 12345
        assert len(v.get_connections()) == 0


if __name__ == "__main__":
    unittest.main(module="graph_list", exit=False)
