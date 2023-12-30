# product of array except self
# Leet Code Problem: https://leetcode.com/problems/product-of-array-except-self/description/
'''

'''

# Approach 1: Prefix Sum and Post Fix Sum
def productExceptSelf(self, nums: List[int]) -> List[int]:
    # length of the array
    n = len(nums)
    # multiplier from start which will not include the current iterating index
    prefix_product = 1
    # multiplier from end which will not include the current iterating index
    postfix_product = 1
    # result array to store the multiplied value
    result = [0]*n

    # Compute prefix as we are computing product of left elements of the array from current element
    for i in range(n):
        result[i] = prefix_product
        prefix_product *= nums[i]
    # Compute postfix as we are computing product of right elements of the array from current element
    for i in range(n-1,-1,-1):
        result[i] *= postfix_product
        postfix_product *= nums[i]
    
    # since postfix and prefix is computed on same result array return it
    return result


# Approach 2:  using hashset
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    if len(nums) == 1:
        return nums[0]

    nonZeroProduct = 1
    zeroHashSet = set()
    result = []

    for i in range(n):
        if nums[i]!=0:
            nonZeroProduct*=nums[i]
        else:
            zeroHashSet.add(i)
    
    for i in range(n):
        if nums[i] == 0:
            if len(zeroHashSet) == 1:
                result.append(nonZeroProduct)
            else:
                result.append(0)
        elif nums[i] != 0:
            if len(zeroHashSet) > 0:
                result.append(0)
            else:
                result.append(nonZeroProduct//nums[i])
    
    return result