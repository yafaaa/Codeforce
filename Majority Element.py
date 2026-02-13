from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = len(nums)//2
        d = Counter(nums)
        return [k for k, v in d.items() if v>c][0]

        
