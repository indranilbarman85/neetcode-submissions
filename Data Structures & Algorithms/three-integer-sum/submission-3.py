class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for a in range(n - 2):
            if nums[a] > 0:              # sorted: nothing left can reach 0
                break
            if a > 0 and nums[a] == nums[a - 1]:   # skip duplicate anchors
                continue

            i, j = a + 1, n - 1
            while i < j:
                total = nums[a] + nums[i] + nums[j]
                if total > 0:
                    j -= 1
                elif total < 0:
                    i += 1
                else:
                    res.append([nums[a], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:  # skip dup left
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:  # skip dup right
                        j -= 1
        return res