# Date : 06/25/19
# 使用贪心算法Greedy Algorithm方式进行判断
# 1.首先枚举列表中的元素，如果第i+1天的价格比第i天的价格高，则在第i天买入然后在第i+1天卖出
# 2.判断时要注意使用的天数应为：总天数-2，因为最后一天不需要买入
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:return 0
        days = len(prices) - 1
        profit = 0
        for i,v in enumerate(prices):
            if i <= days - 1 and v < prices[i+1]:
                profit += prices[i+1] - v
        return profit