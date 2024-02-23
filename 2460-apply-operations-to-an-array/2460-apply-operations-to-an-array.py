class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n):
            if i+1<=n-1 and nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        for k in nums:
            if k==0:
                nums.remove(k)
                nums.append(0)
        return nums