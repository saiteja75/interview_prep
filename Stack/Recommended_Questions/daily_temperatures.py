# daily-temperatures
# https://leetcode.com/problems/daily-temperatures/description/
'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

# Approach 1: Stack
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    st = []
    n = len(temperatures)
    res = [0]*n
    for i in range(n-1,-1,-1):
        while(st and temperatures[st[-1]]<=temperatures[i]):
            st.pop()
        if len(st) == 0:
            res[i] = 0
        else:
            res[i] = st[-1]-i
        st.append(i)
    return res