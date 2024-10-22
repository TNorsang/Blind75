from collections import deque

def right_side_view(root):
    result = []
    queue = deque([root])
    while queue:
        q_len = len(queue)
        right_side = None
        for _ in range(q_len):
            curr_node = queue.popleft()
            if curr_node:
                right_side = curr_node
                queue.append(curr_node.left)
                queue.append(curr_node.right)
        if right_side:
                result.append(right_side.val)
    return result
