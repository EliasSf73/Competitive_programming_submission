from collections import Counter
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
             
        winners=[match[0] for match in matches]
        losers=[match[1] for match in matches]
      
            
        win_count=Counter(winners)
        lose_count=Counter(losers)
        
        no_lose=[player for player in win_count if player not in lose_count]
        one_lose=[player for player,count in lose_count.items() if count==1]
        
        no_lose.sort()
        one_lose.sort()
        return [no_lose,one_lose]


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   