# combinations
# https://leetcode.com/problems/combinations/description/
'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
'''


# Approach 1: recursion [NOT READABLE]
def combine(n: int, k: int) -> List[List[int]]:
    res = []
    def compute(arr,index,curr,k,n,res):
        if index == k:
            res.append(arr)
            return
        for j in range(index+1,n+1):
            if(j>curr):
                arr1 = arr[:]
                arr1.append(j)
                compute(arr1,index+1,j,k,n,res)
    for i in range(1,n+1):
        compute([i],1,i,k,n,res)
    return res

# Approach 2: backtrack
def combine(n: int, k: int) -> List[List[int]]:
    ans = []
    def bt(idx, comb):
        if len(comb) == k:
            ans.append(comb[:])
            return
        for i in range(idx, n + 1):
            comb.append(i)
            bt(i + 1, comb)
            comb.pop()
    bt(1, [])
    return ans