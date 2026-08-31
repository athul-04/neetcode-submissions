class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0: return ""

        encodedStr="#%*"+"#%*".join(strs)
        return encodedStr

    def decode(self, s: str) -> List[str]:
        if len(s)==0: return []
        return s.split("#%*")[1:]
