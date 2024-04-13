# subtree-of-another-tree
# https://leetcode.com/problems/subtree-of-another-tree/
'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

'''

# Approach 1: DFS Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Same(self, p, q):
        if p and q:
            return p.val == q.val and self.Same(p.left, q.left) and self.Same(p.right, q.right)
        return p is q
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root == None:
            return False
        if self.Same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

# Approach 2: BFS