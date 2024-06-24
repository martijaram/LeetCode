# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        speed1 = head
        speed2 = head
        
        
        while (speed2 and speed2.next):
            speed2 = speed2.next.next
            speed1 = speed1.next
            
            
        return speed1
            
        
        