class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRow(row):
            numlist = [x for x in row if x!="."]
            if len(numlist) != len(set(numlist)):
                return False
            else:
                return True
                
        for row in board:
            if not checkRow(row):
                return False

        matrix = board
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for col in matrix:
            if not checkRow(col):
                return False 
            print(col)
        print("\n")
        print("\n")
        print("\n")
        
        for x in range(3):
            mat1,mat2,mat3 = [],[],[]
            mat = matrix[3*x:(3*x)+3]
            row = []
            for y in range(3):
                mat1 += mat[y][0:3]
                mat2 += mat[y][3:6]
                mat3 += mat[y][6:9]
            if not (checkRow(mat1) and checkRow(mat2) and checkRow(mat3)):
                return False 
        
        return True