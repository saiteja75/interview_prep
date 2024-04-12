# lowest-common-ancestor-of-a-binary-search-tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

'''


# Approach 1: Recursive DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return 
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
        

# Approach 2: Iterative
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        while root:
            if root.val > large:  # p, q belong to the left subtree
                root = root.left
            elif root.val < small:  # p, q belong to the right subtree
                root = root.right
            else:  # Now, small <= root.val <= large -> This is the LCA between p and q
                return root
        return None 