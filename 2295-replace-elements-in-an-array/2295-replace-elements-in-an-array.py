class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        mapper={value:idx for idx,value in enumerate(nums)}
        
        for key,value in operations:
           
            if key in mapper:
                ind=mapper[key]
                nums[ind]=value
            del mapper[key]
            if value not in mapper:
                mapper[value]=ind
        
        return nums