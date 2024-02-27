class Solution(object):
    def findDiagonalOrder(self, mat):
        
        
        if not mat or not mat[0]:
            return []

   
        N, M = len(mat), len(mat[0])
        result, intermediate = [], []

 
        for d in range(N + M - 1):
            del intermediate[:]
  


            if d < M:  
                r, c = 0, d
            else:  
                r, c = d - M + 1, M - 1


            while r < N and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1


            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        

        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n=len(mat[0]) # n  columns
#         m=len(mat) # m rows
        
#         new=[ ]
#         move_up=True
#         row,column=0,0
        
#         while row<m and column<n:
#             if move_up:#going from bottom left to top right
#                 while row>0 and column<n-1:
#                     new.append(mat[row][column])
#                     row-=1
#                     column+=1
#                 new.append(mat[row][column])
#                 if column==n-1:# last element of the diagonal
#                     row+=1
#                 else:
#                     column+=1
                    
                
#             else:# going from top right to bottom left
#                 while column>0 and row>m-1:
#                     new.append(mat[row][column])
#                     column-=1
#                     row+=1
#                 new.append(mat[row][column])
#                 if row==m-1:
#                     column+=1
#                 else:
#                     row+=1
#         return new
                
                    