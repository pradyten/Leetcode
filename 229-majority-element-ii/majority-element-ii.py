class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        ans = []
        for i in nums:
            count[i]+=1

        for key, value in count.items():
            if value > len(nums)//3:
                ans.append(key)

        return ans