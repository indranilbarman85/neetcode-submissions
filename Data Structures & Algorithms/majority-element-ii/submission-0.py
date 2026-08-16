class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict

        d_count=defaultdict(int)
        lst=[]
        for  num in nums:
            d_count[num]+=1
            
        for key,value in d_count.items():
            if value>len(nums)/3:
                lst.append(key)
        return lst