# coin-change
# https://leetcode.com/problems/coin-change/description/
'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

# Approach 1: Recursion (TLE)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def change(coins,amount):
            if amount < 0:
                return float('inf')
            
            if amount == 0:
                return 0
            
            mini = float('inf')
            for coin in coins:
                mini = min(mini,change(coins,amount-coin))
            return 1+mini
        value = change(coins,amount) 
        if  value == float('inf'):
            return -1
        return value
        
# Approach 2: Dynamic Programming top-down
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def change(coins,amount,memo):
            if amount in memo:
                return memo[amount]
            if amount < 0:
                return float('inf')
            
            if amount == 0:
                return 0
            
            mini = float('inf')
            for coin in coins:
                mini = min(mini,change(coins,amount-coin,memo))
            memo[amount] = 1+mini
            return memo[amount]
        memo = {}
        value = change(coins,amount,memo) 
        if  value == float('inf'):
            return -1
        return value
        
        
# Approach 3: Dynamic Programming Bottom-Up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')]*(amount+1)
        memo[0] = 0
        for coin in coins:
            if coin<amount:
                memo[coin] = 1
        for cost in range(1,amount+1):
            if memo[cost] == float('inf'):
                for i in coins:
                    if cost-i >=0:
                        memo[cost] = min(memo[cost],1+memo[cost-i])
        if memo[amount] == float('inf'):
            return -1
        return memo[amount]

        
