class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        small = min(len(word1),len(word2))
        ans = ""
        for i in range(small):
            ans+=(word1[i]+word2[i])

        if small == len(word1):
            ans+=word2[small:]
        else:
            ans+=word1[small:]

        return ans