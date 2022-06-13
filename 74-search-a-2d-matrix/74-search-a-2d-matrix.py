class Solution:
    def lower_bound(self, m, t):
        lo,hi = 0, len(m) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if m[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f = [matrix[i][0] for i in range(len(matrix))]
        col = self.lower_bound(f, target)
        if matrix[col][0] > target:
            col -= 1
        row = self.lower_bound(matrix[col], target)
        #print(col, row)
        return matrix[col][row] == target
