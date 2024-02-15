class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        s1=set(a)
        s2=set(b)
        s3=s1 | s2
        return len(s3)