class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        j=len(s1)
        s1=sorted(s1)
        while j<=len(s2):
            if sorted(s2[i:j])==s1:
                return True
            i+=1
            j+=1

        return False
        