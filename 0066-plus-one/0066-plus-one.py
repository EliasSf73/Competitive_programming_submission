class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit=0
        multiple=1
        for i in range(len(digits)-1,0,-1):
            digit+=digits[i]*multiple
            # print(digit)
            multiple*=10
        digit+=digits[0]*multiple+1
           
   
        
        
        print(digit)
        
        array=[]
        while digit>0:
            remainder=digit%10
            array.append(remainder)
            digit=digit//10
            
        return array[::-1]