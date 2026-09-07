class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        start=prices[0]
        profit=0

        for i in range(1,len(prices)):
            if prices[i]-start <0:
                start=prices[i]
                continue
            
            profit=max(profit,prices[i]-start)
        print(profit)
        return profit

        