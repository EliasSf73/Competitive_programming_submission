class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        matrix=[list(x) for x in strs]
        m=len(matrix) #rows
        n=len(matrix[0]) #columns
        deleted=0
        for c in range(n):
            for r in range(1,m):
                if matrix[r-1][c]>matrix[r][c]:
                    deleted+=1
                    break
                
        
        return deleted
        