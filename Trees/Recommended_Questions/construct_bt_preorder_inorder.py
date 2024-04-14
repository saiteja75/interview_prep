# construct-binary-tree-from-preorder-and-inorder-traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return
        value = preorder.pop(0)
        node = TreeNode(value)
        index = inorder.index(value)
        node.left = self.buildTree(preorder,inorder[:index])
        node.right = self.buildTree(preorder,inorder[index+1:])
        return node
        