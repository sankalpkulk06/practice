"""
Leetcode 160: Intersection of Two Linked Lists

Question:
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Example 1:
Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
Output: Intersected at '8'
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

    def getIntersectionNode(self, headA, headB):
        """
        Approach:
        - pointer a : traverse through the list and when you encounter the end, set pointer a to head B and traverse 
        - pointer b : traverse through the list and when you encounter the end, set pointer b to head A and traverse 
        
        wherever they meet is the intersection point.
        because if we do this according to the example, it takes 9 steps for both pointers to reach the c1
        """
        
        # init pointers
        pointerA = headA
        pointerB = headB

        # traverse
        while pointerA != pointerB:
            if pointerA:
                pointerA = pointerA.next
            else:
                pointerA = headB
            if pointerB:
                pointerB = pointerB.next
            else:
                pointerB = headA
        
        return pointerA

if __name__ == "__main__":
    # create a linked list: 4 -> 1 -> 8 -> 4 -> 5
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next
    print("List A:")
    headA.printList(headA)
    print("List B:")
    headB.printList(headB)
    print("Intersection node:", headA.getIntersectionNode(headA, headB).val)
    