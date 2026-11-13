'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        parantheses_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []
        for ch in s:
            if ch in parantheses_map.values():
                stack.append(ch)

            elif ch in parantheses_map.keys():
                if not stack:
                    return False
                if stack[-1] == parantheses_map[ch]:
                    stack.pop()

                else:
                    return False
        return len(stack) == 0


'''
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(n)
'''