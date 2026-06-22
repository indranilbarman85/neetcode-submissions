from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def_dict=defaultdict(list)
        for word in strs:
            def_dict["".join(map(str,sorted(word)))].append(word)
        return list(def_dict.values())
        