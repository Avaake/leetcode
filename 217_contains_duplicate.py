from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = Counter(nums)
        return any(num > 1 for num in nums_dict.values())