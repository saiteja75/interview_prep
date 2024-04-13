#  binary-tree-maximum-path-sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

# Approach 1: recursion DFS if negative sum in left or right reset to 0 to just consider root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def pathSum(node,maxi):
            if node == None:
                return 0
            
            leftSum = max(0,pathSum(node.left,maxi))
            rightSum = max(0,pathSum(node.right,maxi))
            maxi[0] = max(node.val+leftSum+rightSum,maxi[0])
            return node.val+max(leftSum,rightSum)
        maxi = [float('-inf')]
        pathSum(root,maxi)
        return maxi[0]
    

from collections import defaultdict
class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = float('-inf')
        stack, last, d = [], None, defaultdict(int)
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack[-1]        
            if node.right and last != node.right:
                root = node.right
            else:
                # Consume the node
                node = stack.pop()
                last = node
                d[node] = max(max(d[node.left], d[node.right]) + node.val, 0)
                res = max(res, d[node.left] + d[node.right] + node.val)
                
        return res
        