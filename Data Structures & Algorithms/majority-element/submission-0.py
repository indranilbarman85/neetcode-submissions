class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict 
        import math
        dd=defaultdict(int)
        thresh= math.floor(len(nums)/2)
        for num in nums:
            dd[num] += 1
            if dd[num]>thresh:
                return num
        