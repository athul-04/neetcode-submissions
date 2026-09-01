class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        
        for i in range(len(strs)):
            sorted_str="".join(sorted(strs[i]))
            mp[sorted_str]=mp.get(sorted_str,[])
            mp[sorted_str].append(i)
        
        ans=[]
        for indxs in mp.values():
            temp=[]
            for i in indxs:
                temp.append(strs[i])
            ans.append(temp)

        return ans

        