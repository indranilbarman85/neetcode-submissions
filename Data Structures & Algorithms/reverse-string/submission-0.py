class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        d=''
        i=0
        lgth=len(s)
        while i<lgth//2:
            d = s[i]
            s[i]=s[lgth-1-i]
            s[lgth-1-i]=d
            i+=1


