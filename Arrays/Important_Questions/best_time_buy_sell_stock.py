# best time to buy and sell stock
# LeetCode Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''

def maxProfit(prices: List[int]) -> int:
    # buy variable is to track the stock buying by the stock at minimal price so we are delcaring with infinity
    buy = float('inf')
    # Initializing profit to zero as if there no max profit we need to return 0
    profit = 0

    # Iterate through stock prices
    for value in prices:
        # update the buy value if the curr value is minimum
        buy = min(buy,value)
        # Check and update the profit if profit is more with buy and curr value update it
        profit = max(profit,value-buy)

    # return the profit
    return profit