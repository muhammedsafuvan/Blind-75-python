'''
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

# solution 1

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

'''
Time & Space Complexity
Time complexity: O(n^2)
Space complexity: O(1)
'''

# solution 2

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in visited:
                return [visited[complement], i]
            visited[num] = i
        return []


'''
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(n)
'''