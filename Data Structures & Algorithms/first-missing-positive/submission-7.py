class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lst=set(nums)

        min_z=min([v for v in lst if v>=0], default=1)

        if min_z>1 or  min_z is None:
            return 1
        while min_z in lst:
            min_z+=1
        
        return min_z