class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row=0, col=matrix.length-1;
        while (row < matrix[0].length && col >= 0) {
            if (matrix[col][row] > target) col--;
            else if (matrix[col][row] < target) row++;
            else return true;
        }
        return false;
    }
}