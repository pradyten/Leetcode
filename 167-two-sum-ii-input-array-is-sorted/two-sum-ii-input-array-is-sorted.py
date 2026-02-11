class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dict:
                return [dict[target-numbers[i]], i+1]
            else:
                dict[numbers[i]] = i+1