"""
Leetcode 83: Remove Duplicates from Sorted List

Question:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]
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
    
    def deleteDuplicates(self, head):
        """
        Approach:
        - if next is same as curr, then curr.next = curr.next.next
        else, curr = curr.next  
        """
        # init
        curr = head

        # traverse
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
    
if __name__ == "__main__":
    # create a linked list: 1 -> 1 -> 2
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    print("Original list:")
    head.printList(head)
    print("List after removing duplicates:")
    head.deleteDuplicates(head)
    head.printList(head)