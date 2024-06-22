# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return head
        
        past = head        
        head = past.next
        past.next = None
        temp = head
        
        while temp:
            temp = head.next
            
            head.next = past
            past = head
            head = temp    
        
        return past