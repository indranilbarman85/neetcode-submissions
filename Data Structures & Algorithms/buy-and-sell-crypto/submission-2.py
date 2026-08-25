class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i=0
        j=1
        maxP=0
        while i <len(prices)-1 and j<len(prices):
            print(f"{i},{j}")
            if prices[i]>=prices[j]:
                i=j
                j+=1
            else:
                maxP=max(maxP,prices[j]-prices[i])
                j+=1
        return maxP