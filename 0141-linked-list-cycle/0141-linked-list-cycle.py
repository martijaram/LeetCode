# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    possibles = []
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        self.possibles = []
        return self.meh(head)
        
        
        
        
        
        
    def meh(self, head: Optional[ListNode]):
        if (id(head) in self.possibles):
            print(head.val)
            print(self.possibles)
            return True
        
        if (head):
            self.possibles.append(id(head))
            return self.meh(head.next)
            
        else:
            return False
        
        