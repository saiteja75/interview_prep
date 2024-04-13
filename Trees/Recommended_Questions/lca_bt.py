# lowest-common-ancestor-of-a-binary-tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
      return root

    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)

    if l and r:
      return root
    return l or r
  


  class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        que = deque([root])
        parent = {root: None}
        
        while que:
            node = que.popleft()
            
            if node.left:
                que.append(node.left)
                parent[node.left] = node
            
            if node.right:
                que.append(node.right)
                parent[node.right] = node
            
            if p in parent and q in parent:
                break
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q:
            if q in ancestors:
                return q
            q = parent[q]