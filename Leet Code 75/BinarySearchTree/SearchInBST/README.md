# Search in a Binary Search Tree

Initially I used a BFS to traverse through the nodes and return the node if the node matches the value which has a time complexity of O(n) since it is going through every single node.

```
if not root:
            return None
        if root.val == val:
            return root

        def bfs(node):
            queue = deque([node])
            while queue:
                curr_node = queue.popleft()
                if curr_node.val == val:
                    return curr_node
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            return None
        node = bfs(root)
        return node
```

A more optimal approach is to traverse through the nodes based on the value of the root node. If root is larger than search value then we go left since left of root is always smaller in a Binary Search Tree this is same the opposite direction. Time Complexity is O(logn) for this approach since we are only traversing through half of the tree. Space Complexity is O(logn) as well since the space is proportional the height of tree.

```
if not root:
    return None
if root.val == val:
    return root

if root.val > val:
    node = self.searchBST(root.left,val)
if root.val < val:
    node = self.searchBST(root.right,val)

return node
```
