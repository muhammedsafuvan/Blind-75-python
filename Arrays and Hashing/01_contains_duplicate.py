'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.


'''

# solution 1
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


'''
Time & Space Complexity
Time complexity: O(n)
  
Space complexity: O(n)
'''

# solution 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


'''
Time & Space Complexity
Time complexity: O(n)
  
Space complexity: O(n)
'''