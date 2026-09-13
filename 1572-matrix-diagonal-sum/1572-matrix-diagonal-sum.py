class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[n - i -1][i]
        if n % 2 != 0:
            k = n//2
            ans -= mat[k][k]
        return ans