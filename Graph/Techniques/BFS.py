# BFS for a graph

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visited = [False]*(V)
        
        qu = [0]
        res = []
        visited[0]=True
        while(qu):
            v = qu.pop(0)
            res.append(v)
            for i in adj[v]:
                if visited[i] == False:
                    visited[i] = True
                    qu.append(i)
        return res