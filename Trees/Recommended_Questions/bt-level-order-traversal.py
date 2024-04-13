# binary-tree-level-order-traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

'''

# Approach 1: BFS Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        currLevel = [root]
        nextLevel = []
        res = [[root.val]]

        while(currLevel):
            curr = currLevel.pop(0)

            if curr.left:
                nextLevel.append(curr.left)
            if curr.right:
                nextLevel.append(curr.right)
            
            if len(currLevel) == 0 and nextLevel:
                res.append([i.val for i in nextLevel])
                currLevel,nextLevel = nextLevel,currLevel
        return res
    

# APPROACH 2: DFS Recursion
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        count = 0

        def level(count , root):
            if root == None :
                return 

            if len(result) <= count:
                result.append([])    
            
            result[count].append(root.val)
            count += 1
            level(count , root.left)
            level(count , root.right) 

        level(count , root)
        return result
        