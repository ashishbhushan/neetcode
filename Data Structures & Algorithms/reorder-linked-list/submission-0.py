# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        s_head = head
        while s_head is not None:
            stack.append(s_head)
            s_head = s_head.next
        
        left = head
        right = head

        while right is not None and right.next is not None:
            left = right
            right = right.next
            stack[-1].next = None
            last = stack.pop()
            if right == last or left == last:
                break
            left.next = last
            last.next = right
            