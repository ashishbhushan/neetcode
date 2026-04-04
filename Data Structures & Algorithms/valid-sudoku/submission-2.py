class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        def checkRow(row):
            numlist = [x for x in row if x!="."]
            if len(numlist) != len(set(numlist)):
                return False
            else:
                return True
                
        # for row in board:
        #     if not checkRow(row):
        #         return False

        # matrix = [row[:] for row in board]
        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # for col in matrix:
        #     if not checkRow(col):
        #         return False 

        # for x in range(3):
        #     mat1,mat2,mat3 = [],[],[]
        #     mat = matrix[3*x:(3*x)+3]
        #     row = []
        #     for y in range(3):
        #         mat1 += mat[y][0:3]
        #         mat2 += mat[y][3:6]
        #         mat3 += mat[y][6:9]
        #     if not (checkRow(mat1) and checkRow(mat2) and checkRow(mat3)):
        #         return False 

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(n):
            for j in range(n):
                elm = board[i][j]
                if elm==".":
                    continue
                if elm in row[i]:
                    return False
                else:
                    row[i].add(elm)
                if elm in col[j]:
                    return False
                else:
                    col[j].add(elm)
                if elm in box[(i // 3) * 3 + (j // 3)]:
                    return False
                else:
                    box[(i // 3) * 3 + (j // 3)].add(elm)

        
        return True