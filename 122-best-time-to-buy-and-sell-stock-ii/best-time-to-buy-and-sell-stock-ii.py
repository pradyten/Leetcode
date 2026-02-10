class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 0, 0
        i, j = 0, 0
        n = len(prices)
        while i < n-1:
            
            if buy == 0 and prices[i+1]>prices[i]:
                buy = prices[i]
                print(i)
                j = i
                while prices[j+1]>prices[j]:
                    j+=1
                    if j == n-1:
                        break
                    print(j)
                sell = prices[j]
                profit += (sell - buy)
                buy = 0
                j+=1
                i=j
            else:
                i+=1

        if buy != 0:
            sell = prices[i]
            profit += (sell - buy)

        return profit

            
        