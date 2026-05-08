# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            group_tail = self.get_group_tail(group_prev, k)
            if not group_tail:
                break
            group_next = group_tail.next
        
            prev, curr = group_tail.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            group_head = group_prev.next
            group_prev.next = group_tail
            group_prev = group_head
        
        return dummy.next

    def get_group_tail(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr