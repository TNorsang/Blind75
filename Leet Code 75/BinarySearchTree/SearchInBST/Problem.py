def searchBST(root, val):
    if not root:
        return None
    if root.val == val:
        return root

    if root.val > val:
        node = searchBST(root.left,val)
    if root.val < val:
        node = searchBST(root.right,val)
    
    return node