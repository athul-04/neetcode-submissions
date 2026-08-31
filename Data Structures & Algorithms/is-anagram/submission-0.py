class Solution:
    def counter(self,mp:dict,s:str):
        for i in s:mp[i]=mp.get(i,0)+1
        return mp
    def isAnagram(self, s: str, t: str) -> bool:
        mp1={}
        mp2={}
        return self.counter(mp1,s)==self.counter(mp2,t)

        