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
        numSpaces = (len(line)-1)/2

        if numSpaces > 0:
            alloc = int(-(-spaceRemaining//numSpaces))
            for i in range(1,len(line),2):
                alloc = int(-(-spaceRemaining//numSpaces))
                if spaceRemaining < alloc:
                    line[i] = line[i]+" "*spaceRemaining
                else:
                    line[i] = line[i]+" "*alloc
                    spaceRemaining -= alloc
        else:
            line[0] = line[0] + " "*(maxWidth-len(line[0]))

        return ''.join(line)




# Test Case
runSolution = Solution()

print(runSolution.fullJustify(["What","must","be","acknowledgment","shall","be"],16))

'''
["Give  me  my  Romeo; and,",
 "when  he  shall die, Take",
 "him  and  cut  him out in",
 "little stars, And he will",
 "make  the  face of heaven",
 "so   fine   That  all  the", 10
 "world  will  be  in  love",
 "with  night  And  pay  no",
 "worship   to   the garish",
 "sun.                     "]
'''
'''
["Give  me  my  Romeo; and,",
 "when  he  shall die, Take",
 "him  and  cut  him out in",
 "little stars, And he will",
 "make  the  face of heaven",
 "so   fine  That  all  the", 9
 "world  will  be  in  love",
 "with  night  And  pay  no",
 "worship   to  the  garish",
 "sun.                     "]
'''