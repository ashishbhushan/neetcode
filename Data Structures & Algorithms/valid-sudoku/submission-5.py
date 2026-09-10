class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row = [set() for _ in range(n)]
        col = [set() for _ in range(n)]
        box = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row[i]:
                    return False
                else:
                    row[i].add(num)
                if num in col[j]:
                    return False
                else:
                    col[j].add(num)
                if num in box[(i//3*3)+(j//3)]:
                    return False
                else:
                    box[(i//3*3)+(j//3)].add(num)
        
        return True