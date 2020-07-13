"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

         ***********
            use 2 stacks
            push to stack 1
            pop stack 1 and push it to stack 2
            this reverses the order of the first stack
         *********
"""
from singly_linked_list import LinkedList
import sys
sys.path.append('../singly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None

# class Queue:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
#         self.storage = LinkedList()
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             self.size -=1
#             return self.storage.remove_head()
#         else:
#             return None

"""
Stretch goal:
"""

class Two_Stack_Queue ():
    def __init__(self):
        # 1. Create 2 stacks
        self.stack_1 = []
        self.stack_2 = []
        # 2. Push elements onto stack 1
    def enqueue(self, element):
        self.stack_1.append(element)

    def dequeue(self):

        if len(self.stack_2) == 0:
            # 3. Check if stack 1 is empty. If it IS EMPTY raise an error
            if len(self.stack_1) == 0:
                raise IndexError("Queue is empty. Try again later.")

            # 4. If it IS NOT empty - Pop last element and push to stack2. Repeat until stack 1 IS EMPTY.
            while len(self.stack_1) > 0:
                last_stack_1_element = self.stac_1.pop()
                self.stack_2.append(last_stack_1_element)

            # 5. When stack 1 is empty check if stack2 IS empty. 
            # If it IS NOT EMPTY pop the last element and return it
            # Repeat until stack 2 is empty
            return self.stack_2.pop()



       

