from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter=Counter(arr)
        treshold=len(counter)
        print(treshold)
       
        output=[]
        for key,value in counter.items():
            if value==1:
                output.append(key)
        if  (not arr) or (k>len(output)):
            return ''
        return output[k-1]
       
        
        