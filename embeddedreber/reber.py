from node import Node
from edge import Edge

class Reber(object):
    """The graph object is a collection of nodes connected by edges.

    Parameters
    ----------
    alphabet : list
        A list of strings that represent the alphabet and it's placement in the Reber edges.

    Attributes
    ----------
    word : str | None
        After 'simulate' is called a word is created and storred here.

    nodes : list
        List of Node objects that are part of the Reber.

    """


    def __init__(self, alphabet):

        self.alphabet = alphabet
        self.word = None
        self.nodes = [Node() for nodenum in range(8)]

        # Used to print additional details to standard out.
        self.verbose = False


    def create_edges(self):
        """Convenience function to create the neccessary edges for the Reber grammar.
        """

        self.edge1 = Edge(self.alphabet[0], self.nodes[0], self.nodes[1])
        self.edge2 = Edge(self.alphabet[1], self.nodes[1], self.nodes[2])
        self.edge3 = Edge(self.alphabet[2], self.nodes[2], self.nodes[2])
        self.edge4 = Edge(self.alphabet[3], self.nodes[2], self.nodes[3])
        self.edge5 = Edge(self.alphabet[4], self.nodes[3], self.nodes[4])
        self.edge6 = Edge(self.alphabet[5], self.nodes[1], self.nodes[5])
        self.edge7 = Edge(self.alphabet[6], self.nodes[3], self.nodes[5])
        self.edge8 = Edge(self.alphabet[7], self.nodes[5], self.nodes[5])
        self.edge9 = Edge(self.alphabet[8], self.nodes[5], self.nodes[6])
        self.edge10 = Edge(self.alphabet[9], self.nodes[6], self.nodes[3])
        self.edge11 = Edge(self.alphabet[10], self.nodes[6], self.nodes[4])
        self.edge12 = Edge(self.alphabet[11], self.nodes[4], self.nodes[7])


    def simulate(self):
        """ Traverses the Reber grammar graph to generate a word.
        """

        reber_word = []
        current_node = self.nodes[0]

        while current_node != self.nodes[-1]:

            current_node.traverse()
            reber_word.append(current_node.edge_traversals[-1].letter)
            current_node = current_node.next_node

        self.word = ''.join(reber_word)

        if self.verbose:
            print(self.word)


class EmbeddedReber(Reber):
    """
    Parameters
    ----------
    alphabet : list
        A list of strings that represent the alphabet and it's placement in the Reber edges.

    Attributes
    ----------
    word : str | None
        After 'simulate' is called a word is created and storred here.

    nodes : list
        List of Node objects that are part of the embedded Reber grammar.

    rebers : list
        List of Reber objects that are part of the embedded Reber grammar.
    """


    def __init__(self, alphabet):
        super(EmbeddedReber, self).__init__(alphabet)

        self.nodes = [Node() for nodenum in range(4)]
        self.rebers = [Reber(alphabet), Reber(alphabet)]
        [reber.create_edges() for reber in self.rebers]


    def create_edges(self):
        """Convenience function to create the neccessary edges for an embedded Reber grammar.
        """

        self.edge1 = Edge(self.alphabet[0], self.nodes[0], self.nodes[1])
        self.edge2 = Edge(self.alphabet[1], self.nodes[1], self.rebers[0].nodes[0])
        self.edge3 = Edge(self.alphabet[1], self.rebers[0].nodes[-1], self.nodes[2])
        self.edge4 = Edge(self.alphabet[5], self.nodes[1], self.rebers[1].nodes[0])
        self.edge5 = Edge(self.alphabet[5], self.rebers[1].nodes[-1], self.nodes[2])
        self.edge6 = Edge(self.alphabet[11], self.nodes[2], self.nodes[-1])


    def simulate(self):
        """ Traverses the embedded Reber grammar to generate a word.
        """

        super().simulate()