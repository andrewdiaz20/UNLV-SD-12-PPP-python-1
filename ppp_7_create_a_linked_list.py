class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.refernece = reference

    # node1 = Node(5)
    # print(node1.data)
    # node2 = Node(11)
    # node1.reference = node2
    # print(node1.data, node1.refernce)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse_list(self):
        if self.head ==None:
            print("No List to traverse")
        else:
            current_node = self.head        