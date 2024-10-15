class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next= next

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")

node_a.next = node_b
node_b.next = node_c
node_c.next = node_d

def traverse_linked_list(root):
    if not root:
        return
    
    current_node = root

    while current_node:
        print(current_node.val, end="")
        current_node = current_node.next
    

traverse_linked_list(node_a)