# Delete Node In A BST

Understanding BST properties is very important for this question.

I started off by finding the node within the tree by traversing through the left or right subtree based on if the root.val is less or greater than the key value input.

This method is better than going through each subtree since it divides the tree in half, which optimizes the time complexity to O(logn) vs O(n).

Then I used a helper function to find the in-order successor which is also O(logn) because we only need to worry about finding the left-most leaf node in the right subtree starting from the value to be deleted.

Time Complexity: O(log n) Balanced tree so only traversed through half of tree.
Space Complexity: O(log n) Since it uses recursion, space is proportional to the height of the tree.
