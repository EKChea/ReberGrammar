class Edge(object):
    """A vector that connects two nodes.

    Parameters
    ----------
    node_one : Node object
        Movements are unidirectional from node_one to node_two.

    node_two : Node object
        Node that terminatates the edge.  The object that node_one will point two in this vertex.

    Attributes
    ----------
    letter : str
        The value that is tied to this edge. The value will be stored as part of the Reber.word
        attribute if the edge is traversed.

    """

    def __init__(self, letter, node_one=None, node_two=None):
        
        self.node_one = node_one
        self.node_two = node_two

        self.letter = letter
        self.node_one.edges.append(self)