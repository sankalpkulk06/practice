"""
Linked List Introduction

Time Complexity: O(n), where n is number of nodes in the linked list.
Auxiliary Space: O(n) because of recursive stack space.

Space Complexity: O(1) because we are not using any extra space.
"""

# constructor to initialize a new node with data
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

    # function to traverse and print the singly linked list
    def traverseListIterative(self, head):
        while head is not None:
            print(head.data, end="")
            if head.next is not None:   
                print(" -> ", end="")
            head = head.next
        print()
    
    def traverseListRecursive(self, head):
        if head is None:
            return
        print(head.data, end="")
        if head.next is not None:
            print(" -> ", end="")
        self.traverseListRecursive(head.next)

    def insertAtBeginning(self, head, data):
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    def insertAtEnd(self, head, data):
        new_node = Node(data)
        if head is None:
            return new_node
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return head

    def insertAfter(self, head, data, position):
        new_node = Node(data)
        if head is None:
            return new_node
        
        cur = head
        while cur is not None:
            if cur.data == position:
                new_node.next = cur.next
                cur.next = new_node
                return head
            cur = cur.next
        return head

    def deleteAtBeginning(self, head):
        if head is None:
            return head
        return head.next
    
    def deleteAtEnd(self, head):
        if head is None:
            return head
        if head.next is None:
            return None
        current = head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
        return head
    
    def deleteAfter(self, head, position):
        if head is None:
            return head
        current = head
        while current is not None:
            if current.data == position:
                current.next = current.next.next
                return head
            current = current.next
        return head


if __name__ == "__main__":

    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    # traverse and print the linked list
    head.traverseListIterative(head)
    head.traverseListRecursive(head)

    # insert at beginning
    head = head.insertAtBeginning(head, 5)
    print("\nAfter inserting at beginning:")
    head.traverseListIterative(head)

    # insert at end
    head = head.insertAtEnd(head, 50)
    print("After inserting at end:")
    head.traverseListIterative(head)

    # insert after (new node after 20)
    head = head.insertAfter(head, 35, 20)
    print("After inserting after 20:")
    head.traverseListIterative(head)

    # delete at beginning
    head = head.deleteAtBeginning(head)
    print("After deleting at beginning:")
    head.traverseListIterative(head)

    # delete at end
    head = head.deleteAtEnd(head)
    print("After deleting at end:")
    head.traverseListIterative(head)

    # delete after (delete node after 35)  
    head = head.deleteAfter(head, 35)
    print("After deleting after 35:")
    head.traverseListIterative(head)