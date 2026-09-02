class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for i in range(0,len(tokens)):
            if len(stack)>1 and tokens[i] in ("*","-","/","+"):
                first=stack.pop()
                second=stack.pop()

            if tokens[i]=="*":
                stack.append(second*first)
            
            elif tokens[i]=="+":
                stack.append(second+first)
            elif tokens[i]=="-":
                stack.append(second-first)
            elif tokens[i]=="/":
                stack.append(int(second/first))
            else:
                stack.append(int(tokens[i]))
            
        
        
        return int(stack[0])
                


        