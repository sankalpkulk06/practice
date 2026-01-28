"""
leetcode 21: Merge Two Sorted Lists

Question:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def printList(head):
        while head is not None:
            print(head.val, end=" ")
            head = head.next
        print()
    
    def printNode(self, head):
        print("Node value: ", head.val)
    
    @staticmethod
    def mergeTwoLists(list1, list2):  
        """
        Approach:
        - create a dummy node to store the merged list
        - create a pointer to the dummy node
        - traverse the lists and compare the values of the nodes
        - add the smaller value node to the merged list
        - move the pointer to the next node
        - return the dummy node's next node
        """
        # init
        dummy = ListNode()
        current = dummy
        
        # traverse the lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # if list1 is not empty, add the remaining nodes to the merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # return the merged list
        return dummy.next

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    merged_list = ListNode.mergeTwoLists(list1, list2)
    ListNode.printList(merged_list)