class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[i for i in nums if i>0]
        neg=[j for j in nums if j<0]
        output=[]
        for k in range(len(pos)) :
            output.append(pos[k])
            output.append(neg[k])
            
        return output