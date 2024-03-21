class Solution:
    def convert(self, s: str, numRows: int) -> str:
        outArray = []
        for i in range(numRows):
            outArray.append(list())
        
        direction = 0 # 0 is down, 1 is up
        i = 0

        for letter in s:
            if i > numRows-1:
                return s
            
            outArray[i].append(letter)

            if direction == 0:
                i += 1
            if direction == 1:
                i -= 1

            if i == numRows-1 or i == 0:
                direction = 1-direction
        
        output = ""
        for row in outArray:
            output += ''.join(row)

        return output
                


# Test Case
runSolution = Solution()

print(runSolution.convert("AB",1))