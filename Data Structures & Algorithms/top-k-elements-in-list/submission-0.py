class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for i in nums: mp[i]=mp.get(i,0)+1
        cnt=[]
        for key,val in mp.items():cnt.append([key,val])

        cnt.sort(key=lambda x : x[1],reverse=True)
        ans=[cnt[i][0] for i in range(k)]
        
        return ans
        
        