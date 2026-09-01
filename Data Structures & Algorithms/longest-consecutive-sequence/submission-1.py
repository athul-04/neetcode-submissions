import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=[]
        if len(nums)==0: return 0
        for i in nums:
            heapq.heappush(arr,i)
        maxi=1
        prev=heapq.heappop(arr)
        maxi_flow=1
        while len(arr)>0:
            curr=heapq.heappop(arr)
            if curr-1==prev:
                maxi_flow+=1
    
            elif curr==prev:
                continue
            else:
                maxi_flow=1
            prev=curr
            maxi=max(maxi,maxi_flow)
        print(maxi)

        return maxi
        