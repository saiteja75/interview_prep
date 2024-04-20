
# Appraoch 1: Priority Queue
import heapq

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, src):
        #code here
        # Create a priority queue to store vertices that
        # are being preprocessed
        pq = []
        heapq.heappush(pq, (0, src))
    
        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * V
        dist[src] = 0
    
        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            d, u = heapq.heappop(pq)
    
            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
    
        return dist





#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
        

# Approach 2: BFS simulating priority queue greedy
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        distances = [float('inf')]*V
        visited = [False]*V
        distances[S] = 0
    
        def updateDistance(vertex):
            if visited[vertex] == False:
                visited[vertex] = True
                for edge in adj[vertex]:
                    if distances[vertex]+edge[1]<distances[edge[0]]:
                        distances[edge[0]] = distances[vertex]+edge[1]
                mini = float('inf')
                index = -1
                for i in range(V):
                    if mini>distances[i] and visited[i] == False:
                        mini = distances[i]
                        index = i
                updateDistance(index)
            else:
                return
        updateDistance(S)
        return distances