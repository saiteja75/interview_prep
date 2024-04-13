# same-tree
# https://leetcode.com/problems/same-tree/description/
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

'''

# Approach 1: recursion DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        if (p == None and q != None) or (p != None and q == None):
            return False
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    

# Approach 2: iteration BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q == None and p == None:
            return True
        
        qu = [[p,q]]

        while(qu):
            curr = qu.pop()

            if curr[0] == None and curr[1] == None:
                return True
            elif (curr[0] == None and curr[1] != None) or (curr[0] != None and curr[1] == None):
                return False

            if curr[0].val == curr[1].val:
                if curr[0].left or curr[1].left:
                    qu.append([curr[0].left,curr[1].left])
                
                if curr[0].right or curr[1].right:
                    qu.append([curr[0].right,curr[1].right])
            else:
                return False
        
        return True
    

def isSameTree(p,q):
    stack =[(p,q)]
    while stack:
        p,q = stack.pop()
        if not p and not q:
            continue
        elif (not p or not q) or (p.val !=q.val):
            return False
        stack.extend([(q.right,p.right),(q.left,p.left)])
    return True
        