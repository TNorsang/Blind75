# Binary Tree RIght Side View

This question is a bit tricky, it is ambiguous.
It wants you to imagine your self on the right side of the binary tree and print out the nodes
you can see from that perspective.

However the input examples are given such that they are not clear.
ex: [1,2,3,null,5,null,4]
1
2 3
5 4
With the given tree, it is obvious to print out the right nodes of the tree only, but what is confusing is if the right node is missing lets say node 4, then you have to print out node 5 since it is visible from the right view.

I had to look up the solution after a bit of thinking.

Solution uses BFS and loops through each level, using the length of current queue, and then sets the right side to be the current node, if there are three nodes in that level then the last iteration will set the right side node to be that node.

Time Complexity: O(n) Even with an inner loop you are going through the inputs exactly once.
Space Complexity: O(n) Queue uses O(n) space as well as the result list.
