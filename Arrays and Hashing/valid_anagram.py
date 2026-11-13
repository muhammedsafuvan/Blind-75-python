'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.


'''

#solution 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

'''
Time & Space Complexity
Time complexity: O(nlogn + mlogm)
Space complexity: O(n+m)

'''


# solution 2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}
        
        for i in s:
            count_s[i] = count_s.get(i,0)+1
            count_t[i] = count_t.get(i,0)+1

        return count_s == count_t

''' 
Time & Space Complexity
Time complexity: O(n+m)
Space complexity: O(1) (since the size of the hash maps is limited by the number of unique characters, which is constant for a fixed character set)
'''

