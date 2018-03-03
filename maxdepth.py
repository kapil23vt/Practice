def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    if not root:
        return 0
    
    queue = []
    height = 0
    queue.append(root)
    
    while queue:
        size = len(queue)
        print (size)
        height = height + 1
        
        
        for i in range(size):
            # takeout the node
            node = queue.pop(0)
            
            # add left and right node
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
    return height

root = [1,2,3,4,5]
print (maxDepth(root))