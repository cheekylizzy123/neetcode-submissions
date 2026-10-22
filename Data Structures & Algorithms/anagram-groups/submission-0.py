class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))   #make words 

            if temp in seen:
                seen[temp].append(strs[i])  
            else:
                seen[temp] = [strs[i]]
        
        final_list= []
        for item in seen:
            final_list.append(seen[item])
        return final_list

                
            

        



        
                


        