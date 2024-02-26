from collections import Counter
class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        counter=Counter(nums)
        ones=counter[1]
        zeros=counter[0]
        
        pointer=1
        left_zeros=0
        right_ones=ones
        count={0:ones}
        while pointer<n+1:
            if nums[pointer-1]==0:
                left_zeros+=1
            else:
                right_ones-=1
            count[pointer]=left_zeros+right_ones
            pointer+=1
        # print(count)
        sorted_tuples = sorted(count.items(), key=lambda item: item[1], reverse=True)
        max_value = sorted_tuples[0][1]
        max_keys = [key for key, value in sorted_tuples if value == max_value]
            
        return max_keys   
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n=len(nums)
       
#         counter={}
          
#         for k in range(n+1):
          
#             counter[k]=Counter(nums[:k])[0]+Counter(nums[k:])[1]
                
       

            
#         return max_keys
#         # print(left)
#         # print(right)
#         # print(counter)
        
            