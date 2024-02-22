class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        first,last=0,len(s)-1
        while first<last:
            s[first],s[last]=s[last],s[first]
            first,last=first+1,last-1
       