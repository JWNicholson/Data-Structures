"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check value exist
        if value >= self.value:
            # check if there is a right child
            if self.right is not None:
                # if right child exists insert value
                self.right.insert(value)
            else:
                # if no right child exist create one
                self.right = BSTNode(value)
        elif value < self.value:
            # check if there is a left child
            if self.left is not None:
                 # if right child exists insert value
                self.left.insert(value)
            else:
                # if no left child exist create one
                self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    #####################################
    #if value is in right child return true and break else return false
    #if root node doesnt have the value return false
    #check if their is a right child
    #check if value in left child
    #if value exist return true and break
    def contains(self, target):
        #check tree for root value
        if self.value == target:
            return True

        if target > self.value:
            if self.right is not None:
                return self.right.contains(target)

            elif target < self.value:
                if self.left is not None:
                    return self.left.contains(target)

            else:
                return False


    # Return the maximum value found in the tree

    # check if there is a right child - if True, get it
    # ^ ^ ^ ^ ^ .................... - if False get the left one
    # else return self
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()

        else:
            return self.value

    # Call the function `fn` on the value of each node

    # set value of fn
    # check if left node exists and call fn of each self on left nodes
    #do same for right
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    #check if the node is empty
    #if node not empty, check right - if right is not empty 
    # keep checking left & right nodes until reaching the final childrens
    #recursively check backwards to the left
    def in_order_print(self, node):
        # if self.left is not None:
        #     self.left.in_order_print(self.left)

        #     #visit the node
        #     print(node.value)

        # if self.right is not None:
        #     self.right.in_order_print(self.right)

## alternate version - less code
        if node.left:
            self.in_order_print(node.left)

        print(node.value)

        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    #make a queue
    # while the queue is not empty -
    # dequeue from the the front of the queue
    # enqueue the children of the current into the queue

    def bft_print(self, node):
        q_nodes = queue.Queue(0)# https://docs.python.org/3/library/queue.html
        q_nodes.put(node)

        # empty() returns true if queue is empty
        while not q_nodes.empty(): #(while not True)
            current_nodes = q_nodes.get()
            print(current_nodes.value)

            if current_nodes.left:
                q_nodes.put(current_nodes.left)

            if current_nodes.right:
                q_nodes.put(current_nodes.right)

        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    # https://docs.python.org/3/library/queue.html?highlight=lifoque#queue.LifoQueue -- Last In First Out
    def dft_print(self, node):
        q_nodes = queue.LifoQueue()
        q_nodes.put(node)

        while not q_nodes.empty():
            current_node = q_nodes.get()
            print(current_node.value)

            if current_node.right:
                q_nodes.put(current_node.right)
                
            if current_node.left:
                q_nodes.put(current_node.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
