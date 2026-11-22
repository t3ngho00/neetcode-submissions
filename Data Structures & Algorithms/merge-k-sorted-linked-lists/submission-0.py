# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
            
        dummy = ListNode()
        cur = dummy
        if len(lists) == 2:
            head1 = lists[0]
            head2 = lists[1]
        
            while head1 and head2:
                if head1.val < head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next
            
            while head1:
                cur.next = head1
                head1 = head1.next
                cur = cur.next
                
            while head2:
                cur.next = head2
                head2 = head2.next
                cur = cur.next
            return dummy.next

        # if len(lists) != 0,1,2
        m = len(lists)//2
        left = self.mergeKLists(lists[0:m])
        right = self.mergeKLists(lists[m:len(lists)])
        return self.mergeKLists([left, right])
            
