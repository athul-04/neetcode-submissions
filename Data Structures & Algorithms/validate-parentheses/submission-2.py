class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2!=0):return False
        stack=[]
        mp={
            "[":"]",
            "(":")",
            "{":"}"
        }
        for i in s:
            
            if len(stack)!=0 and mp.get(stack[-1])==i:
                
                stack.pop()
            else:
                stack.append(i)

        return len(stack)==0



        







        