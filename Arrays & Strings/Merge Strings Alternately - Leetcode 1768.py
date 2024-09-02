class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(len(word1)):

            if i >= len(word2):
                res += word1 [i:]
                return res
            
            res += word1[i] + word2[i]
        
        if len(word2) > len(word1):
            res += word2[i+1:]
            return res
        return res

# Test cases
sol = Solution()

word1="abc"
word2 = "pqr"
print(sol.mergeAlternately(word1, word2))
assert sol.mergeAlternately(word1, word2) == "apbqcr"

word1 = "ab"
word2 = "pqrs"
print(sol.mergeAlternately(word1, word2))
assert sol.mergeAlternately(word1, word2) == "apbqrs"

word1 = "abcd"
word2 = "pq"
print(sol.mergeAlternately(word1, word2))
assert sol.mergeAlternately(word1, word2) == "apbqcd"