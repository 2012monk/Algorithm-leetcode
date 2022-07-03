class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(m)
        ret = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ret[j][n-1-i]= m[i][j]
        for i in range(n):
            for j in range(n):
                m[i][j] = ret[i][j]