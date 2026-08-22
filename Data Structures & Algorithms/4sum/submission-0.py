class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:      # skip dup first anchor
                continue
            # pruning: smallest / largest reachable with a fixed
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break                                  # sorted: only grows
            if nums[a] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue                               # a too small, skip it

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:  # skip dup second anchor
                    continue
                if nums[a] + nums[b] + nums[b + 1] + nums[b + 2] > target:
                    break
                if nums[a] + nums[b] + nums[n - 2] + nums[n - 1] < target:
                    continue

                i, j = b + 1, n - 1
                need = target - nums[a] - nums[b]
                while i < j:
                    s = nums[i] + nums[j]
                    if s > need:
                        j -= 1
                    elif s < need:
                        i += 1
                    else:
                        res.append([nums[a], nums[b], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
        return res