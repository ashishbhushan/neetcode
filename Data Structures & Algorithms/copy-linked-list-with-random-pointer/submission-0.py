"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copydict = {None: None}
        curr = head
        while curr:
            copydict[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = copydict[curr]
            copy.next = copydict[curr.next]
            copy.random = copydict[curr.random]
            curr = curr.next

        return copydict[head]