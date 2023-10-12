class Node():
    '''This class represents a single Node.'''

    def __init__(self, key):
        self.key = key
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):
        if self.rChild != None:
            self.rChild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.key)

        if self.lChild != None:
            self.lChild.print_node(level + 1)
    
      # In-order traversal - left, center, right
    def inOrder(self, aNode):
        if (aNode != None):
            aNode.inOrder(aNode.lChild)
            print(aNode.key, end=" ")
            aNode.inOrder(aNode.rChild)

    # Pre-order traversal - center, left, right
    def preOrder(self, aNode):
        if (aNode != None):
            print(aNode.key, end=" ")
            aNode.preOrder(aNode.lChild)
            aNode.preOrder(aNode.rChild)

    # Post-order traversal - left, right, center
    def postOrder(self, aNode):
        if (aNode != None):
            aNode.postOrder(aNode.lChild)
            aNode.postOrder(aNode.rChild)
            print(aNode.key, end=" ")

    def bst_size(self, node):
        # if node.rChild == None and node.lChild == None:
        #     return 0 
        # elif node.rChild == None:
        #     return 1 + self.bst_size(node.lChild)
        # elif node.lChild == None:
        #     return 1 + self.bst_size(node.rChild)
        # else:
        #     return 1 + self.bst_size(node.lChild) + self.bst_size(node.rChild)
        
        if node == None:
            return 0
        else:
            return 1 + self.bst_size(node.lChild) + self.bst_size(node.rChild)



class BST():
    '''This class represents a Binary Search Tree.'''

    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    # Search for a node with the key
    def search(self, key):
        current = self.root
        while ((current != None) and (current.key != key)):
            if (key < current.key):
                current = current.lChild
            else:
                current = current.rChild
        return current

    # Insert a node in the tree
    def insert(self, val):
        newNode = Node(val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
# seearch 
            while (current != None):
                parent = current
                if (val < current.key):
                    current = current.lChild
                else:
                    current = current.rChild
# insert 
            if (val < parent.key):
                parent.lChild = newNode
            else:
                parent.rChild = newNode


    # Find the node with the smallest value
    def minimum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.lChild
        return parent

    # Find the node with the largest value
    def maximum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.rChild
        return parent

    # Delete a node with a given key
    def delete(self, key):
        deleteNode = self.root
        parent = self.root
        isLeft = False

        # If empty tree
        if (deleteNode == None):
            return False

        # Find the delete node
        while ((deleteNode != None) and (deleteNode.key != key)):
            parent = deleteNode
            if (key < deleteNode.key):
                deleteNode = deleteNode.lChild
                isLeft = True
            else:
                deleteNode = deleteNode.rChild
                isLeft = False

        # If node not found
        if (deleteNode == None):
            return False

        # Delete node is a leaf node
        if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
            if (deleteNode == self.root):
                self.root = None
            elif (isLeft):
                parent.lChild = None
            else:
                parent.rChild = None

        # Delete node is a node with only left child
        elif (deleteNode.rChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.lChild
            elif (isLeft):
                parent.lChild = deleteNode.lChild
            else:
                parent.rChild = deleteNode.lChild

        # Delete node is a node with only right child
        elif (deleteNode.lChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.rChild
            elif (isLeft):
                parent.lChild = deleteNode.rChild
            else:
                parent.rChild = deleteNode.rChild

        # Delete node is a node with both left and right child
        else:
            # Find delete node's successor and successor's parent nodes
            successor = deleteNode.rChild
            successorParent = deleteNode

            while (successor.lChild != None):
                successorParent = successor

                successor = successor.lChild

            # Successor node right child of delete node
            if (deleteNode == self.root):
                self.root = successor
            elif (isLeft):
                parent.lChild = successor
            else:
                parent.rChild = successor

            # Connect delete node's left child to be successor's left child
            successor.lChild = deleteNode.lChild

            # Successor node left descendant of delete node
            if (successor != deleteNode.rChild):
                successorParent.lChild = successor.rChild

                successor.rChild = deleteNode.rChild

        return True
    

    ################# My Code #########################

    # sort the items in the tree
    def sort(self):
        sorted_list = []

        if self.root:
            self.in_order_traversal(self.root, sorted_list)

        return sorted_list
 
    # helper function for sort
    def in_order_traversal(self, node, sorted_list):
        if node:
            self.in_order_traversal(node.lChild, sorted_list)
            sorted_list.append(node.key)
            self.in_order_traversal(node.rChild, sorted_list)

    # find the median of the values in the tree
    def bst_median(self):
        sorted_list = self.sort()
        size = self.root.bst_size(self.root)
        if size % 2 == 1:
            median = sorted_list[size//2]
        else:
            median = (sorted_list[size//2] + sorted_list[size//2 + 1]) / 2

        return median
    
    # find the height of a tree
    def height(self):
        # height of the tree is the larger of the height of the left and the right child
        # base case is that a node has no children
        return self._height(self.root)

    # helper function for height
    def _height(self, node):
        if node:
            return 1 + max(self._height(node.rChild), self._height(node.lChild))
        else:
            return 0

    # determine whether a tree is balanced
    def is_balanced(self):
        ans = self._is_balanced(self.root)

        if ans >= 0:
            return True
        else:
            return False

    # helper function for balance
    def _is_balanced(self, node):
        if not node:
            return 0 
        else:
            right = self._is_balanced(node.rChild)
            left = self._is_balanced(node.lChild)
            if right < 0 or left < 0:
                return -1
            if abs(left-right) > 1:
                return -1
            if right > left: 
                return 1 + right
            else: 
                return 1 + left
            
###############################
#                             #
#   Example run of a BST run  #
#                             #
###############################

def main():
    bst = BST()

    bst.insert(10)
    bst.insert(40)
    bst.insert(5)
    bst.insert(15)
    bst.insert(22)
    bst.insert(4)

    bst.print(2)
    print("##############")
    bst.delete(10)
    bst.print(2)
    print("##############")

    print("Print In-Order")
    bst.root.inOrder(bst.root)

    print()
    print("Print Pre-Order")
    bst.root.preOrder(bst.root)

    print()
    print("Print Post-Order")
    bst.root.postOrder(bst.root)

    size = bst.root.bst_size(bst.root)
    print("Size of the BST:", size)

    sorted_elements = bst.sort()
    print("Sorted elements of the BST:", sorted_elements)

    median = bst.bst_median()
    print("Median element of the BST:", median)

    tree_height = bst.height()
    print("Height of the BST:", tree_height)

    is_balanced = bst.is_balanced()
    if is_balanced:
        print("The BST is balanced.")
    else:
        print("The BST is not balanced.")

if __name__ == '__main__':
    main()
