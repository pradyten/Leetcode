class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        s1 = set()
        s2 = set()
        longest = 0

        for i in nums:
            s1.add(i)

        for x in s1:
            print("Hello")
            if x in s2:
                continue
            s2.add(x)
            i = 1
            total = 0
            while True:
                if x - i in s1:
                    s2.add(x-i)
                    i+=1
                else:
                    total = i
                    i = 0
                    break
            
            while True:
                if x + (i+1) in s1:
                    s2.add(x+i+1)
                    i+=1
                else:
                    total += i
                    break
            
            if total > longest:
                longest = total

        return longest
            