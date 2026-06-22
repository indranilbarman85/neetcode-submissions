class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small=strs[0]
        for x in strs:
            if len(x)<len(small):
                small=x
        output=""
        for i in range(0,len(small)+1):
            if len(set(x[0:i] for x in strs))>1:
                return(output)
            else:
                output=small[0:i]
        return(output)
        