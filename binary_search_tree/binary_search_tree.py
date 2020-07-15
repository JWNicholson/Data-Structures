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
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
