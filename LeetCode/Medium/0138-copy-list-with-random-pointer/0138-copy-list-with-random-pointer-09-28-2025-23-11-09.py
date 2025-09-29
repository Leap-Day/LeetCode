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
        # keep a list of each deep copied pointer 
        # O(n) space
        # or do this recursively which takes up O(n) space on the stack
        # even if we do this recursively, what about cycles

        randomNodes = { None : None}

        cur = head

        while cur:
            new = Node(cur.val)
            randomNodes[cur] = new
            cur = cur.next

        cur = head
        while cur:
            copy = randomNodes[cur]
            copy.next = randomNodes[cur.next]
            copy.random = randomNodes[cur.random]
            cur = cur.next

        return  randomNodes[head]