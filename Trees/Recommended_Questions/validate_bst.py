# validate-binary-search-tree
# https://leetcode.com/problems/validate-binary-search-tree/description/
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''


# Approach 1:DFS
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur_node, lower_bound, upper_bound):
            # Base Case
            if cur_node == None:
                return True
            
            # If Current_Node's Value Not Lies in the Range,, Return False
            if not lower_bound < cur_node.val < upper_bound:    
                return False
            
            # For Making Recursive Calls,, We nned to Go to the Left Side && Right Side
            # At Left Sub-Tree,, Lower Bound not changes,, Upper Bound becomes the Current_Node(Parent)
            # At Right Sub-Tree,, Upper Bound not Changes,, Lower Bound becomes the Current_Node(Parent)

            return (dfs(cur_node.left, lower_bound, cur_node.val) and 
                    dfs(cur_node.right, cur_node.val, upper_bound))

        # Main Func
        lower_bound = float('-inf') # Initialized with -ve Infinity
        upper_bound = float('inf') # Initialized with +ve Infinity
        return dfs(root, lower_bound, upper_bound)
    



# Approach 2:BFS
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            lower_bound = float('-inf') # Initialized with -ve Infinity
            upper_bound = float('inf') # Initialized with +ve Infinity

            # Let's First Add, Current_Node & lower_bound & upper_bound as a Entity in Queue
            queue = deque( [ (root, lower_bound, upper_bound) ] )

            while queue:
                # Take Out Top Guy
                cur_node, low, high = queue.pop()

                # Checking Condition of Range
                if not low < cur_node.val < high:    
                    return False
                
                # If Current Node has Left,, Then Append that Node, by Changing the Bounds
                if cur_node.left: 
                    queue.append( [cur_node.left, low, cur_node.val] )
                
                # If Current Node has Right,, Then Append that Node, by Changing the Bounds
                if cur_node.right: 
                    queue.append( [cur_node.right, cur_node.val, high] )
            
            # If While Loop Completes Successfully, without Returning False, We return True
            return True
        
        # Main
        return bfs(root)