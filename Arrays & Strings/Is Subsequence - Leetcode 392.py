class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indx = []
        for i in range(len(s)):
            indx.append(t.find(s[i]))
            if indx[-1] < 0:
                return False
            t = t[indx[-1] + 1:]
        return True