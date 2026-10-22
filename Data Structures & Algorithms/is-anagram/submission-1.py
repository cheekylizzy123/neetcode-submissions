class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letterw1 = {}
        for c in s:
            if c not in letterw1:
                letterw1[c] = 1
            else:
                letterw1[c] += 1 
        
        letterw2={}
        for d in t:
            if d not in letterw2:
                letterw2[d] = 1
            else:
                letterw2[d] += 1 

        for item in letterw1:
            if item not in letterw2:
                return False
            else:
                if letterw1[item] != letterw2[item]:
                    return False 
        
        return True 
            
        