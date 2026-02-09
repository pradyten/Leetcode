class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*(n+1)
        suffix = [1]*(n+1)  
        ans = []
        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1]*nums[i-1]

        for j in range(len(nums)-1, 0, -1):
            suffix[j-1] = suffix[j]*nums[j]

        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        
        return ans
