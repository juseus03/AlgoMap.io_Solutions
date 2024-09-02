class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
        res = 0

        for i in range(len(s)):

            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
                continue
            res += roman[s[i]]
        return res



sol = Solution()

s = "III"
print(sol.romanToInt(s))
assert sol.romanToInt(s) == 3

s = "LVIII"
print(sol.romanToInt(s))
assert sol.romanToInt(s) == 58

s = "MCMXCIV"
print(sol.romanToInt(s))
assert sol.romanToInt(s) == 1994
