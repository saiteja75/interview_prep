# binary-tree-right-side-view
# https://leetcode.com/problems/binary-tree-right-side-view/description/
'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

'''

# Approach 1: BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        res.append(root.val)
        currLevel = [root]
        nextLevel = []

        while(currLevel):
            node = currLevel.pop(0)

            if node.left:
                nextLevel.append(node.left)
            
            if node.right:
                nextLevel.append(node.right)

            if len(currLevel) == 0 and nextLevel:
                res.append(nextLevel[-1].val)
                currLevel,nextLevel = nextLevel,currLevel
        return res 
    


class Solution:
    # The plan here is to dfs the tree, right-first
    # (opposite of  the usual left-first method), and
    # keeping track of the tree levels as we proceed. The 
    # first node we visit on each level is the right-side view 
    # node. We know it's the first because the level will be
    # one greater than the length of the current answer list.

    def rightSideView(self, root: TreeNode) -> List[int]:
        ans =[]
        
        def dfs(node =root,level=1):
            if not node: return
            
            if len(ans) < level: 
                ans.append(node.val)
            dfs(node.right,level+1)         #  <--- right first
            dfs(node.left ,level+1)         #  <--- then left

            return 

        dfs()
        return ans