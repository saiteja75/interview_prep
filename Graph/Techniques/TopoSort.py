'''
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every 
directed edge u-v, vertex u comes before v in the ordering.

'''
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        st = []
        visited = [False]*V
        def dfs(vertex):
            if visited[vertex] == False:
                visited[vertex] = True
                
                for e in adj[vertex]:
                    dfs(e)
                
                st.append(vertex)
        for i in range(V):
            dfs(i)
        return st[::-1]