class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Set=list(set(nums))
        return len(nums)!=len(Set)
        
        