class Solution:
    def modifiedList(self, nums, head):
        remove_set = set(nums)
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            if curr.val in remove_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next