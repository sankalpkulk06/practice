"""
Leetcode 82: Remove Duplicates from Sorted List II

Question:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
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
        Approach: Dummy Node
        - use two pointers: prev and curr
        - if the curr node is same as next node, skip whole block of duplicates using while loop
        - else, traverse to the next node
        - return the dummy node's next node
        """
        
        # init dummy node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        # traverse
        while curr and curr.next:
            if curr.val == curr.next.val:
                duplicate = curr.val
                while curr and curr.val == duplicate:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        
        return dummy.next

if __name__ == "__main__":
    # create a linked list: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)
    print("Original list:")
    head.printList(head)
    print("List after removing duplicates:")
    result = head.deleteDuplicates(head)
    head.printList(result)