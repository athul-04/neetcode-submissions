class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        
        for i in range(len(strs)):
            sorted_str="".join(sorted(strs[i]))
            mp[sorted_str]=mp.get(sorted_str,[])
            mp[sorted_str].append(strs[i])
        
        ans=[]
        for indxs in mp.values():
            ans.append(indxs)

        return ans

        