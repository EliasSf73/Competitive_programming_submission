from collections import Counter
import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        targets=[]
        counter=Counter(nums)
       
     
        for key in counter:
       
            if counter[key]>math.floor(n/3):
                
                targets.append(key)
                
        return targets