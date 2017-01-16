from src.customCsv import parse_to_array
from src.task import extract_attributes
from src.node import Node
from src.id3 import ID3


dataset = parse_to_array('jogarTenis.data')
attributes = extract_attributes(dataset)

id3 = ID3(dataset, attributes)
root = id3.get_root()

tree = Node(root, dataset)

id3.run(tree)

# dataset = parse_to_array('jogarTenis2.data')
#
# id3 = ID3(dataset, attributes)
# root = id3.get_root()
#
# node = Node(root, dataset)
#
# tree.add_child_node(node)

tree.print_tree()