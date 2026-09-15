class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        FR = False
        FC = False
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            if matrix[i][0] == 0:
                FC = True
                break
        for i in range(c):
            if matrix[0][i] == 0:
                FR = True
                break
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if FR == True:
            for i in range(c):
                matrix[0][i] = 0
        if FC == True:
            for k in range(r):
                matrix[k][0] = 0
        return matrix