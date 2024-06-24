# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        speed1 = head
        speed3 = head
        hmm = True
        
        if (not head.next):
            return head
        elif (not head.next.next):
            return head.next
        elif (not head.next.next.next):
            return head.next
        
        while ((speed1 != speed3 and speed1.next != speed3) or hmm):
            if (not speed3.next):
                speed3 = head.next.next.next
            elif (not speed3.next.next):
                speed3 = head.next.next
            elif (not speed3.next.next.next):
                speed3 = head.next
            else:
                speed3 = speed3.next.next.next
            
            speed1 = speed1.next
            hmm = False
            
            
        return speed1
            
        
        