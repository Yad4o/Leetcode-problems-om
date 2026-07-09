class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        if rows * cols != r * c:
            return mat
        flat = []
        for i in range(rows):
            for j in range(cols):
                flat.append(mat[i][j])
        result = [[0] * c for _ in range(r)]
        index = 0
        for i in range(r):
            for j in range(c):
                result[i][j] = flat[index]
                index += 1
        return result