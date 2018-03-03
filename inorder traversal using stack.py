class Node:
     
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
# Iterative function for inorder tree traversal
# logic 
# for this tree you need to print 4 first
# so stack looks like = [1 2 4]
# now at 4, next left element is None
# so at this point, check length of stack (3)
# stack len not 0, so pop element (4), so stack = [1 2]
# add right of 2 to stack since we need it
# stop doing this when len of stack becomes 0
def inOrder(root):
     
    current = root 
    s = [] 
    flag = False
     
    while(not False):
         
        if current is not None:
            s.append(current)
            current = current.left 
 
        else:
            if(len(s) >0 ):
                current = s.pop()
                print (current.data)
                current = current.right 
            else:
                flag = True
                
 
""" Constructed binary tree is
            1
          /   \
         2      3
       /      
      4       """
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

 
inOrder(root)
