# kth-smallest-element-in-a-bst
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
'''

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        if root is None:
            return -1
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res[k-1] 
        

# Approach 2: BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        st = []
        curr = root
        while(curr or st):
            while curr:
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            res.append(curr.val)
            if len(res) == k:
                return curr.val
            curr = curr.right
        