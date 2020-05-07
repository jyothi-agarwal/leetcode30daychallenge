from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict=Counter(nums)
        for i in nums:
            if dict[i] > abs(len(nums)/2):
                return i
