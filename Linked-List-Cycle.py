'''
Linked List Cycle 

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.
Can you solve it without using extra space?
O(n), O(1)
'''

class Solution(object):

    def detectCycle(self, head):
        if head is None:
            return None

        fast = slow = head
        intersect = None
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                intersect = fast
                break
        
        if not intersect:
            return None
        else:
            print intersect.val
            
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
