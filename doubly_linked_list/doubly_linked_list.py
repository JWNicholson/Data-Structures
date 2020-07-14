"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
import math

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #empty
        if self.head is None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            #not empty
            prev = self.head
            self.head = ListNode(value, None, prev)
            prev.prev = self.head
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        old_node = self.head.value
        self.delete(self.head)
        return old_node

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #empty
        if self.tail is None:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            #not empty
            prev = self.tail # set previous
            self.tail = ListNode(value, prev)
            prev.next = self.tail
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        old_node = self.tail.value
        self.delete(self.tail)
        return old_node

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        if node == self.head:
            #empty 
            if self.head.next is None:
                self.head = None
                self.tail = None

            else:
                # not empty
                self.head = self.head.next
                self.head.prev = None
        elif node == self.tail:
            if self.tail.prev is None:
                self.head = None
                self.prev = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        current = self.head
        max = -math.inf## dont for the - for negative infinity

        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        return max
