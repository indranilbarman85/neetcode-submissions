class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums_set=set(nums)
        
        min_z=min([v for v in nums if v>=0], default=1)

        if min_z>1 or  min_z is None:
            return 1
        while min_z in nums_set:
            min_z+=1
        
        return min_z