# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = ListNode(0)
            head = dummy
            while l1 or l2:
                first = l1.val if l1 else float("inf")
                second = l2.val if l2 else float("inf")
                if first <= second:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next
            return dummy.next

        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            mergedlists = []
            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i+1] if i+1<len(lists) else None
                mergedlists.append(merge(first, second))
            lists = mergedlists
        return lists[0]
        
    