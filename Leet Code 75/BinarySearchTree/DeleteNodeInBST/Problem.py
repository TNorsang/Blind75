def deleteNode(root, key):
    if not root:
        return None

    def find_successor(node): # 6
        least_value = node

        while least_value.left:
            least_value = least_value.left
        return least_value

    if key < root.val:
        root.left = deleteNode(root.left,key) # 
    elif key > root.val:
        root.right = deleteNode(root.right,key)
    elif key == root.val: # 5=5
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        in_order_successor = find_successor(root.right)
        root.val = in_order_successor.val
        
        root.right = deleteNode(root.right, in_order_successor.val)
    return root
