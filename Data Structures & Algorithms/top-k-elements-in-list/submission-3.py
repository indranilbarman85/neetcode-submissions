class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import defaultdict

        count_dict=defaultdict(int)
        for c in range(len(nums)):
            count_dict[nums[c]]+=1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count_dict.items():
            buckets[freq].append(num)
        print(buckets)
        iter=0
        lst=[]
        i=0
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                lst.append(num)
                if len(lst) == k:
                    return lst

        