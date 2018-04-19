class Node:
     def __init__(self):
         self.name = "Node"

def loop_size(node):
    pass

node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(node1.next)