class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i

        for j in range(len(nums)):
            if target-nums[j] in d and j!=d[target-nums[j]]:
                return([j,d[target-nums[j]]])
        