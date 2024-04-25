# course-schedule
# https://leetcode.com/problems/course-schedule/description/
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        visited = [False]*numCourses
        for i in prerequisites:
            adjList[i[0]].append(i[1])
        def dfs(vertex,visited,rs):
            visited[vertex] = True
            rs.add(vertex)
            for i in adjList[vertex]:
                if visited[i] == False:
                    if dfs(i,visited,rs):
                        return True
                elif i in rs:
                    return True
            rs.remove(vertex) 
            return False

        for i in range(numCourses):
            if dfs(i,visited,set([])):
                return False
        return True