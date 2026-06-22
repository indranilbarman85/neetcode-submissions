from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        z=defaultdict(list)
        for x in strs:
            value = "".join(map(str,sorted(x)))
            z[value].append(x)
        return list(z.values())
        