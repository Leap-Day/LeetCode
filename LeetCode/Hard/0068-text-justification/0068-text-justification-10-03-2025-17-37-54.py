class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # greedy
        # dp
        # minimize the number of lines
        # add text up until max width
        # if it exceeds, start adding spaces
        # between each word until we hit maxWidth
        # repeat until no words remain
        
        res = []
        curLineLen = 0
        wordsOnLine = []
        i = 0



        while i < len(words):
            if len(words[i]) + len(wordsOnLine) + curLineLen > maxWidth:
                neededSpaces = maxWidth - curLineLen
                spaces = neededSpaces // max(1, len(wordsOnLine) - 1)
                remainderSpaces = neededSpaces % max(1, len(wordsOnLine) - 1)

                for j in range(max(1, len(wordsOnLine) - 1)):
                    wordsOnLine[j] += " " * spaces
                    if remainderSpaces:
                        wordsOnLine[j] += " "
                        remainderSpaces -= 1

                res.append("".join(wordsOnLine))
                wordsOnLine = []
                curLineLen = 0

            wordsOnLine.append(words[i])
            curLineLen += len(words[i])
            i += 1
            
        lastLine = " ".join(wordsOnLine)
        trailingSpace = maxWidth - len(lastLine)

        res.append(lastLine + " " * trailingSpace)
        
        return res
