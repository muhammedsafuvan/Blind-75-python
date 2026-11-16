'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

'''
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_set = set()
        col_set = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0
        return matrix

'''
Time & Space Complexity
Time complexity: O(m*n)
Space complexity: O(m+n)'''
