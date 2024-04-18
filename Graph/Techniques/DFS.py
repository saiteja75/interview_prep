class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        res = []
        visited = [False]*V
        def dfsUtil(vertex,visited):
            if visited[vertex] == False:
                visited[vertex] = True
                res.append(vertex)
            
                for e in adj[vertex]:
                    dfsUtil(e,visited)
            else:
                return
                
        
        for i in range(V):
            dfsUtil(i,visited)
        return res