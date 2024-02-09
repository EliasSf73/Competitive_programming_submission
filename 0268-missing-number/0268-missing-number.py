class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        lists=[x for x in range(n+1)]
        return sum(lists)-sum(nums)