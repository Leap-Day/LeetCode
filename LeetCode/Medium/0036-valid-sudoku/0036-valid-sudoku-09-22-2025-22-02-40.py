class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for rows in range(9):
            for cols in range(9):
                val = board[rows][cols]
                
                if val == '.':
                    continue
                boxindex = (rows // 3) + (cols // 3) * 3
                
                if val in row[rows] or val in col[cols] or val in box[boxindex]:
                    return False

                row[rows].add(val)
                col[cols].add(val)
                box[boxindex].add(val)
        
        return True
