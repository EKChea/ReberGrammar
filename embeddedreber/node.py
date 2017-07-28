import random

class Node(object):
    """A connecting point for edges.

    Parameters
    ----------
    edges : list or tuple
        (Optional) Edges that the node is connected to.

    Attributes
    ----------
    next_node : Node object or None
        When the traverse function is the next step will be storred as next node.

    edge_traversals : list
        List integers that represent the indices of the 'edges' attribute, and thereby
        which edges were traversed from this node.

    Examples
    --------
    To connect two nodes by an edge.

        >>> from node import Node
        >>> from edge import Edge
        >>> node_one = Node()
        >>> node_one.edges
        []
        >>> node_two = Node()
        >>> node_two.edges
        []
        >>> edge = Edge('A', node_one, node_two)
        >>> node_one.edges
        [<edge.Edge object at 0x00000296D0AC4DA0>]
        >>> node_two.edges # unidirectional, thus an edge is not attached to node_two
        []
        >>> # Flip the order of the edge attachment
        >>> edge = Edge('A', node_two, node_one)
        >>> # Now node_two has a path to travers to node_one
        >>> node_two.edges
        [<edge.Edge object at 0x00000296D0AD4B70>]

    To get all the paths that were traversed.

        >>> from node import Node
        >>> from edge import Edge
        >>> node_one = Node()
        >>> node_two = Node()
        >>> edge = Edge('A', node_one, node_two)
        >>> node_one.traverse()
        >>> node_one.edge_traversals
        [<edge.Edge object at 0x000002919AB14D68>]
        >>> node_one.traverse()
        >>> node_one.edge_traversals
        [<edge.Edge object at 0x000002919AB14D68>, <edge.Edge object at 0x000002919AB14D68>]
    """


    def __init__(self, edges=None):

        self.edges = [] if edges is None else edges
        self.__next_node = None

        # Keeps track of edges traversed
        self.edge_traversals = []


    def traverse(self):
        """Makes a move from the current node to another. The __next_node property is set and
        the edge is catalogued in the form of an integer that represents the index for the edges property.
        """
        if len(self.edges) == 0:
            import pdb; pdb.set_trace()
        assert len(self.edges) > 0, "There is nowhere for node {} to traverse".format(self)

        edgepath = random.randint(1, len(self.edges)) - 1
        self.__next_node = self.edges[edgepath].node_two
        self.edge_traversals.append(self.edges[edgepath])

    @property
    def next_node(self):
        """Retrieves the next_node in the planned traversal."""

        return self.__next_node