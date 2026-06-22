from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def_dict=defaultdict(list)
        for word in strs:
            value = "".join(map(str,sorted(word)))
            def_dict[value].append(word)
        return list(def_dict.values())
        