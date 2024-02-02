class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls=list(s)
        lt=list(t)
        
      
        
        if set(s)!=set(t):
            l=[x for x in t if x not in s]
            if l:
                return l[0]
        else:
            merged=ls+lt
            merged.sort()
            for a in merged:
                if merged.count(a)>1 and merged.count(a)%2 !=0:
                    return a
            
              
                
          
       
        
        
        
        
    
        