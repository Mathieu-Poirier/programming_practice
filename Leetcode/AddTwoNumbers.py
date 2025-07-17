
from typing import Optional


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry: # while l1 or l2 or carry aren't None
        v1 = l1.val if l1 else 0 # if l1 is not None, then v1 is l1.val, otherwise v1 is 0
        v2 = l2.val if l2 else 0 # if l2 is not None, then v2 is l2.val, otherwise v2 is 0

        val = v1 + v2 + carry # add the values and the carry
        carry = val // 10 # carry is integer division of val by 10
        val = val % 10 # val is the remainder of val divided by 10
        current.next = ListNode(val) # create a new node with the value
        current = current.next # move the current pointer to the next node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

# Time complexity: O(max(m, n))
# Space complexity: O(max(m, n))

""" 
Practice writing it out

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10

        current.next = ListNode(val)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

# Time complexity: O(max(m, n))
# Space complexity: O(max(m, n))

Steps:
1. Create a dummy node and a current pointer
2. While l1 or l2 or carry is not None, add the values and the carry
3. Create a new node with the value
4. Move the current pointer to the next node
5. Move the l1 and l2 pointers to the next node
6. Return the dummy.next node
"""