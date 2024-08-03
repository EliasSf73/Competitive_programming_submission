class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if empty string
        if not strs:
            return ''
        
        
        short=min(strs,key=len)
        ln=len(short)
        
        while ln>0:
            found=all(x.startswith(short) for x in strs)
            if found:
                return short
            else:
                short=short[:-1]
                ln-=1
        return ''
     
          
           
         
             
                    
            
       
                    
        