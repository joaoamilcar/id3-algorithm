class Node:
    children = []

    def __init__(self, attribute, subset):
        self.attribute = attribute
        self.subdataset = subset

    def add_child_node(self, node):
        assert isinstance(node, Node)
        self.children.append(node)

    def print_tree(self):
        print(self.subdataset)
        print(self.attribute)
        print(self.children)
        pass

    def __repr__(self):
        return str(self.attribute)