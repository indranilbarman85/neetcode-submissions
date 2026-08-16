class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
            from collections import defaultdict
            seen = defaultdict(int)
            seen[0] = 1          # empty prefix: sum of nothing = 0
            prefix = 0
            count = 0
            for x in nums:
                prefix += x
                count += seen[prefix - k]   # earlier prefixes that complete a K-sum
                seen[prefix] += 1
            return count
        