class Solution:
    def romanToInt(self, s: str) -> int:
        romanMapping = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        result = 0

        for i in range(len(s)):
            if i<len(s)-1 and romanMapping[s[i]] < romanMapping[s[i+1]]:
                result -= romanMapping[s[i]]
            else:
                result += romanMapping[s[i]]

        return result

# Test Case
runSolution = Solution()

print(runSolution.romanToInt("CDLIII"))