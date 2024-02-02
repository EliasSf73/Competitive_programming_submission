class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n=len(word1)
        m=len(word2)
        merged=''
        if n>m:
            for i in range(m):
                merged+=word1[i]
                merged+=word2[i]
            for x in word1[m:]:
                merged+=x
        else:
            for i in range(n):
                merged+=word1[i]
                merged+=word2[i]
            for x in word2[n:]:
                merged+=x
        return merged
            
                    