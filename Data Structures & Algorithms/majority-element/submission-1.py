class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter 
        import math
        thresh= math.floor(len(nums)/2)
        z=Counter(nums)
        key = next((k for k, v in z.items() if v >thresh), None)

        return key
            