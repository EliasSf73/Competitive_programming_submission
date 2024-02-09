class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # if nums is empty or None, return 0
            return 0

        counters = []
        counter = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                if counter:
                    counters.append(counter)
                counter = 0

        if counter:  # if the last element in nums was a 1
            counters.append(counter)
            
        if counters:
            return max(counters)  # Return 0 if counters is empty
        else:
            return 0
