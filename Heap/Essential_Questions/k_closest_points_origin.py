# k-closest-points-to-origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/
'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''

# Approach 1: heap
import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def computeDistance(x,y):
            value = math.pow(x,2)+math.pow(y,2)
            return value

        heap = []
        ans = []
        for i,point in enumerate(points):
            hq.heappush(heap,(computeDistance(point[0],point[1]),i,point))
        
        while k>0:
            value = hq.heappop(heap)
            ans.append(value[2])
            k-=1
        
        return ans
    

# Approach 2: heap refined where we need to store only K elements
import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def computeDistance(x,y):
            value = -(math.pow(x,2)+math.pow(y,2))
            return value

        heap = []
        ans = []
        for i,point in enumerate(points):
            dist = computeDistance(point[0],point[1])
            if len(heap) == k:
                hq.heappushpop(heap,(dist,i,point))
            else:
                hq.heappush(heap,(computeDistance(point[0],point[1]),i,point))
        
        while k>0:
            value = hq.heappop(heap)
            ans.append(value[2])
            k-=1
        
        return ans
        
        
        
        
        
        