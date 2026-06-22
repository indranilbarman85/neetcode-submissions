class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num1=nums.copy()
        num1.extend(nums)
        return num1