class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i, j, count = 0, 0, 0
        n = len(nums)
        prefix = [0]*(n+1)
        freq = defaultdict(int)
        freq[0] = 1
        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
            if (prefix[i] - k) in freq:
                count += freq[prefix[i] - k]
            freq[prefix[i]]+=1

        return count
