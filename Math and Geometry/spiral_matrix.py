'''
Given an m x n matrix, return all elements of the matrix in spiral order.

'''

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        row_start = col_start = 0
        row_end = m-1
        col_end = n-1
        spiral = []
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end+1):
                spiral.append(matrix[row_start][i])

            row_start += 1
            for i in range(row_start, row_end+1):
                spiral.append(matrix[i][col_end])
            col_end -= 1

            if row_start <= row_end:

                for i in range(col_end, col_start-1,-1):
                    spiral.append(matrix[row_end][i])
                row_end -= 1

            if col_start <= col_end:

                for i in range(row_end, row_start-1,-1):
                    spiral.append(matrix[i][col_start])
                col_start += 1
        return spiral

'''
Time & Space Complexity
Time complexity: O(m*n)
Space complexity:
O(1) extra space.
O(m∗n) space for the output list.
'''



            



        