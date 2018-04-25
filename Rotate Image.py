class Solution(object):
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for row in A:
            for i in range(len(row)/2):
                row[i], row[~i] = row[~i], row[i]
