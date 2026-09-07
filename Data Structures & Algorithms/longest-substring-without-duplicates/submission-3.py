class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        if s=="":return 0
        i=0
        seen[s[i]]=i

       
        maxi=0
        for j in range(1,len(s)):
            if s[j] in seen:
                i=max(seen[s[j]]+1,i)
                
            maxi=max(maxi,j-i)
            seen[s[j]]=j
        print(maxi+1)
        return maxi+1
            