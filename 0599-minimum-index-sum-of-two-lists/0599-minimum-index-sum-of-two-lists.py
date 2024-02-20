
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1={elem:index for index,elem in enumerate(list1)}
        
        dict2={elem:index for index,elem in enumerate(list2)}
        dict3={}
        for key in dict1:
            if key in dict2:
                dict3[key]=dict1[key]+dict2[key]
                
        sorted_list = sorted(dict3.items(), key=lambda item: (item[1],item[0]))
        # print('SL',sorted_list)
        
        least_sum=sorted_list[0][1]
        # print('ls',least_sum)
        return [key for key,val in sorted_list if val==least_sum]
       
            
        

           
      
     
        
        
            
    
                
        

       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # counter1=Counter(list1)
        # counter2=Counter(list2)
        # targets={key:counter1[key]+counter2[key] for key in counter1 if key in counter2}
        # return targets
       