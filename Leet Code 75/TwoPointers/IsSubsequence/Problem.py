'''
Pop all leaf nodes and return it's output until there are no nodes left.

If a parent becomes a leaf node, do not pop it out right away.

  
bfs, dfs

bfs : Pre-Order, In-Order, Post-Order

[1,2,4,5,3,4,6]
[4,2,5,1,4,3,6]

If the node has children, what ever is popped you should remember the order, so we can reverse it and append it to the answer at the end.

queue = [1,2,3]
order_parents = [1,2,3]
result = [4,5,4,6]

Append the order_parents to result in reversal.

'''
from collections import deque

class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

  

def remove_leaf_nodes(root):
    order_parents = [] # 1,2,3
    result = [] # 4,5,4,6 
    curr_head = root
    queue = deque([curr_head]) # [5,4,6]
    while queue:
        curr_node = queue.popleft() # 4
        if curr_node.left or curr_node.right:
            order_parents.append(curr_node)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        else:
            result.append(curr_node)
    answer = result.append(order_parents[::-1])
    return answer

    
head = Node(1)
head.left = Node(2)
head.left.left = Node(4)
head.left.right = Node(5)
head.right = Node(3)
head.right.left = Node(4)
head.right.right = Node(6)


answer = remove_leaf_nodes(head)
print(answer)
