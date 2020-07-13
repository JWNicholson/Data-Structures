class Node:
"""
Data:
1. The Value
2. The Next Node
Methods/Behavior/Operations
1. Get value
2. Set value
3.Get next
4.Set next
"""

def __int__(self, value=NONE, next_node=None):
    self.value = value
    self.next_node = next_node

def get_vlaue(self):
    return self.value

def set_value(self, value):
    self.value = value 

def get_next(self):
    return self.next_node

def set_next(self, new_next):
    self.next_node = new_next


class LinkedList:
   """
   Data:
   1. Referecne to head Node
   2. Reference to tail Node

   Behavior/Methods
   1. Add To Tail
   2. Prepend (add a new node and point at Node's next_node at the olf Head: update Head pointer)
   3. Remove Head
   4. Remove Tail
   5. Contains?
   6. Get Maximum?
   """

   def __init__(self):
       self.head = None
       self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        #Empty LL
        if self.head is None:
            return None
        #LL of one item
        if self.head.get_next() is None:
            head = self.head

            self.head = None
            
            self.tail = None

            return head.get_vlaue

        # More than one item
        value - self.head.get_vlaueself.head = self.head.get_next()
        return value
