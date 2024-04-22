# clone-graph
# https://leetcode.com/problems/clone-graph/description/
'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Approach 1:BFS
from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        res = Node(1)
        qu = deque([[node,res]])
        hashMap = {}
        hashMap[node] = res

        while qu:
            curr,decopy = qu.popleft()
            neighbors = []
            for edge in curr.neighbors:
                if hashMap.get(edge,-1) == -1:
                    node = Node(edge.val)
                    neighbors.append(node)
                    hashMap[edge] = node
                    qu.append([edge,node])
                else:
                    neighbors.append(hashMap[edge])
            decopy.neighbors = neighbors
        return res
                
            
# Approach 2: DFS

class Solution:
    
    def helper(self, node, visited):
        if node is None:
            return None
        
        newNode = Node(node.val)
        visited[node.val] = newNode
        
        for adjNode in node.neighbors:
            if adjNode.val not in visited:
                newNode.neighbors.append(self.helper(adjNode, visited))
            else:
                newNode.neighbors.append(visited[adjNode.val])
        
        return newNode
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.helper(node, {})