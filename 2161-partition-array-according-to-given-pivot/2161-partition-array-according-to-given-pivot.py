class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        output=[]
        for elem in nums:
            if elem<pivot:
                output.append(elem)
        for elem in nums:
            if elem==pivot:
                output.append(elem)
        for elem in nums:
            if elem>pivot:
                output.append(elem)
                
        return output
        
                