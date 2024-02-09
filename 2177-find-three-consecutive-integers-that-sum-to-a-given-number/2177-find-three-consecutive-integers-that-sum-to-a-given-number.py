class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
       
        # ans=[]
        # for i in range(num//3-1 ,num//2 ):
        #     if 3*(i+1)==num:
        #         ans.append(i)
        #         ans.append(i+1)
        #         ans.append(i+2)
        # return ans
        if num %3 !=0:
            return []
        else:
            return [num/3 -1, num/3, num/3 +1]
                
        