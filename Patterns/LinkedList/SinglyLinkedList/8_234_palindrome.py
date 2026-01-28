"""
Leetcode 234: Palindrome Linked List

Question:
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printList(self, head):
        while head is not None:
            print(head.val, end=" ")
            head = head.next
        print()
    
    def printNode(self, head):
        print("Node value: ", head.val)
    
    def isPalindrome(self, head):
        """
        Phase 1: find the middle of the list
        Phase 2: reverse the second half of the list
        Phase 3: compare the two halves
        """
        # Phase 1: find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle of the list
        
        # Phase 2: reverse the second half of the list
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        # prev is the new head of the second half of the list

        # Phase 3: compare the two halves
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
    
if __name__ == "__main__":
    # create a linked list: 1 -> 2 -> 2 -> 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print("Original list:")
    head.printList(head)
    print("Is palindrome: ", head.isPalindrome(head))
