'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev


'''
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(1)
'''