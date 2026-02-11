class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        count = defaultdict(int)
        for i in nums:
            if i > 0:
                count[i]+=1
        
        i = 1
        while True:
            if i not in count:
                return i
            else:
                i+=1

        

        