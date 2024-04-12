# invert-binary-tree
# https://leetcode.com/problems/invert-binary-tree/description/
'''
Given the root of a binary tree, invert the tree, and return its root.
'''

# Approach 1: recursive DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        root.left,root.right = root.right,root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

# Approach 2: Iterative BFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        head = root
        if root == None:
            return root
        queue = [root]
        
        while(queue):
            curr = queue.pop(0)
            
            if curr:
                curr.left, curr.right = curr.right, curr.left
            
                queue.append(curr.left)
                queue.append(curr.right)
        return head