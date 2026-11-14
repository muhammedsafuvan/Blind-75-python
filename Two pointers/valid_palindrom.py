'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for ch in s:
            if ch.isalnum():
                new_str+= ch.lower()
        return new_str == new_str[::-1]

'''
Time & Space Complexity
Time complexity: O(n)
  
Space complexity: O(n)
'''