def removeDuplicates(head):
     
     """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
    """
     cur = head
     while cur and cur.next:
        
        if cur.val == cur.next.val:
            cur.next=cur.next.next
        else:
            cur = cur.next
     return head
    