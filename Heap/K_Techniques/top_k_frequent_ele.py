# top-k-frequent-elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
'''

# Approach 1: Heap 
import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        hashMap = {}
        for i in nums:
            if i in hashMap.keys():
                hashMap[i] +=1
            else:
                hashMap[i] = 1
        for key,value in hashMap.items():
            arr.append((-1*value,key))
        
        hq.heapify(arr)
        res = []
        while k>0:
            res.append(hq.heappop(arr)[1])
            k-=1
        
        return res
    

# Approach 2: Heap refined logic:
import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        hashMap = Counter(nums)
        for key,value in hashMap.items():
            hq.heappush(arr,(-1*value,key))
        res = []
        while k>0:
            res.append(hq.heappop(arr)[1])
            k-=1
        
        return res

        

        