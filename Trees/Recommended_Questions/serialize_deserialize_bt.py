# serialize-and-deserialize-binary-tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

'''

# Approach 1: BFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return 'N'
        res = []
        qu = [root]
        while(qu):
            node = qu.pop(0)
            if node:
                res.append(str(node.val))

                qu.append(node.left)
                qu.append(node.right)
            else:
                res.append('N')
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i = 0
        n = len(data)
        if data[i] == 'N':
            return None
        data = data.split(' ')
        root = TreeNode(int(data[i]))
        curr = root
        i+=1
        que = [curr]
        while(que and i<n):
            value = que.pop(0)
            value.left = TreeNode(int(data[i])) if data[i]!='N' else None
            value.right = TreeNode(int(data[i+1])) if i+1<n and data[i+1]!='N' else None
            if value.left:
                que.append(value.left)
            if value.right:
                que.append(value.right)
            i+=2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
    

# Approach 2: DFS

class Codec:

    def serialize(self, root):
        res = []
        def preorder(root):
            if not root:
                res.append('N')
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        data = data.split(',') # now, data = res
        self.i = 0
        def preorder():
            if data[self.i] == 'N':
                self.i += 1
                return None
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = preorder()
            root.right = preorder()
            return root
        
        return preorder()
    
# Time: O(N)
# Space: O(N)