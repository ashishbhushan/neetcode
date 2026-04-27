# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        prev = None
        curr = head
        curr_next = curr.next
        remove_index = length - n
        if remove_index == 0:
            return head.next
        for _ in range(remove_index):
            prev = curr
            curr = curr.next
            curr_next = curr_next.next
        
        curr.next = None
        prev.next = curr_next
        return head