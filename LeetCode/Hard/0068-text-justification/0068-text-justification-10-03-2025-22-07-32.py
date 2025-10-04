class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if len(words[i]) + len(line) + length > maxWidth:
                spaces = maxWidth - length
                neededSpaces = spaces // max(1, len(line) - 1)
                remainderSpaces = spaces % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * neededSpaces
                    if remainderSpaces:
                        line[j] += " "
                        remainderSpaces -= 1

                res.append("".join(line))
                line, length = [], 0

            line.append(words[i])
            length += len(words[i])
            i += 1

        
        lastline = " ".join(line)
        lastline += " " * (maxWidth - len(lastline))
        res.append(lastline) 

        return res




                
        