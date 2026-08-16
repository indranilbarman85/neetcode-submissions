class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lst=set(nums)
        min_p = 1
        while min_p in lst: 
            min_p += 1
        return min_p
        