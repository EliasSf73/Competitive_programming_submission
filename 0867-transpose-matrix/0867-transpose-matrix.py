class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
   
        m=len(matrix[0])
        n=len(matrix)
        new=[[0]*n for _ in range(m)]
        
        for i in range(n):
            for j in range(m):
                new[j][i]=matrix[i][j]
        return new
        