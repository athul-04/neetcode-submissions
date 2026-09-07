class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1={}
        mp2={}
        if len(s1)>len(s2): return False
        for i in s1: mp1[i]=mp1.get(i,0)+1

        for i in range(0,len(s1)):
            mp2[s2[i]]=mp2.get(s2[i],0)+1

        if mp1==mp2:return True

        i=0
        j=len(s1)

        print(mp1)
        # print(mp2)

        while i<j and j<len(s2):
            print(mp2)
            if mp1==mp2: return True
            mp2[s2[i]]-=1
            if mp2[s2[i]]==0: del mp2[s2[i]]
            mp2[s2[j]]=mp2.get(s2[j],0)+1
            
            i+=1
            j+=1
            
        return mp1==mp2




        