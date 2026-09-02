class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temps)

        for ind,t in enumerate(temps):

            while stack and stack[-1][0]<t:
                ans[stack[-1][1]]=(ind-stack[-1][1])
                stack.pop()
            stack.append([t,ind])
        return ans