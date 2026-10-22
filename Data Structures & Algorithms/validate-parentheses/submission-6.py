class Solution:
    def isValid(self, s: str) -> bool:
        # stack implementation with array, LIFO
        if len(s) % 2 != 0:   # if its not even length, immediately false
            return False 

        b_stack = []
        for b in range(len(s)):
            if s[b] == "(" or s[b] == "{" or s[b] == "[":
                b_stack.append(s[b])
            else:
                if not b_stack:
                    return False 
                if s[b] == "}":
                    if b_stack[-1] != "{":
                        return False 
                elif s[b] == "]":
                    if b_stack[-1] != "[":
                        return False 
                else:
                    if b_stack[-1] != "(":
                        return False 

                b_stack.pop()     
        if b_stack:
            return False 
        return True 


                


        
        

