class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original=x
       
        # if x==0:
        #     return True
        if x<0 :
            return False
        li=[]
        while x>0:
            rem=x%10
            x=x//10
            li.append(rem)
        
        # print(li)
        new=0
        
        for i in range(len(li)):
            new+=li[i]*(10**(len(li)-i-1))
        # print(new)
        return new==original 
        