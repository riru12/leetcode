from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        outArray = [[]]
        arrIndex = 0

        for i in range(len(words)):
            if self.subArrayLength(outArray[arrIndex]) == 0:
                outArray[arrIndex].append(words[i])
            elif self.subArrayLength(outArray[arrIndex]) + len(words[i]) + 1 <= maxWidth:
                outArray[arrIndex].append(" ")
                outArray[arrIndex].append(words[i])
            else:
                outArray.append(list())
                arrIndex +=1
                outArray[arrIndex].append(words[i])
        
        for i in range(len(outArray)-1):
            outArray[i] = self.spaceExpander(outArray[i], maxWidth)
        outArray[-1].append(" "*(maxWidth-self.subArrayLength(outArray[-1])))
        outArray[-1] = ''.join(outArray[-1])
        return outArray

    def subArrayLength(self, array: List[str]) -> int: ## returns the total number of characters in an array
        length = 0
        for word in array:
            length += len(word)
        return length
    
    def spaceExpander(self, line: List[str], maxWidth:int) -> int:
        spaceRemaining = maxWidth - self.subArrayLength(line)
        numSpaces = int((len(line)-1)/2)

        if numSpaces > 0:
            baseAlloc = int(spaceRemaining // numSpaces)
            remainder = int(spaceRemaining % numSpaces)

            spaceDistrib = [baseAlloc] * numSpaces
            for i in range(remainder):
                spaceDistrib[i] = spaceDistrib[i]+1

            j = 0
            for i in range(1,len(line),2):
                line[i] = line[i]+" "*spaceDistrib[j]
                j += 1
        else:
            line[0] = line[0] + " "*(maxWidth-len(line[0]))

        return ''.join(line)




# Test Case
runSolution = Solution()

print(runSolution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))

# Take note lines 36-41; efficient way to EVENLY distribute a number n into an array of size m (e.g. 7 into array of size 3 -> [3,2,2]); learned from GPT