'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order
'''

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        visited = {}
        for word in strs:
            cur = ''.join(sorted(word))
            if cur in visited:
                visited[cur].append(word)
            else:
                visited[cur] = [word]
        result = []
        for v in visited.values():
            result.append(v)
        return result

'''
Time & Space Complexity
Time complexity: O(n)
  
Space complexity: O(n)
'''