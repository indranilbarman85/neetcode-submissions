class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        joined=""
        i=min(len(word1),len(word2))
        for j in range(i):
            joined=joined+word1[j]+word2[j]
            
        joined=joined+word1[i:]+word2[i:]

        return joined
