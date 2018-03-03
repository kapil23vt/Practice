INT_MAX = 4294967296
INT_MIN = -4294967296
 
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
 
def isBSTtemp(node):
    return (isBST(node, INT_MIN, INT_MAX))
 
# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBST(node, mini, maxi):
     
    # An empty tree is BST
    if node is None:
        return True
 
    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBST(node.left, mini, node.data -1) and
          isBST(node.right, node.data+1, maxi))
 
# Driver program to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
 
if (isBSTtemp(root)):
    print ("Is BST")
else:
    print ("Not a BST")
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)