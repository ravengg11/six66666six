python class Node:     
    def __init__(self, value, left=None, right=None):        
        self.value = value         
        self.left = left         
        self.right = right  
        
   1) def sum_tree(node):     
            if node is None:         
                return 0     
            else:         
                return node.value + sum_tree(node.left) + sum_tree(node.right)
                
   2) def find_max(root):
    if root is None:
        return None
    elif root.right is None:
        return root.value
    else:
        return find_max(root.right)
        
   3) def find_min_node(node):
   

    
    if not node.left and not node.right:
        return node.val

    
    min_val = node.val
    if node.left:
        left_min = find_min_node(node.left)
        min_val = min(min_val, left_min)

    if node.right:
        right_min = find_min_node(node.right)
        min_val = min(min_val, right_min)

    return min_val
        
  4)  def count_occurrences(root, element):
    if root is None:
        return 0
    count = 1 if root.data == element else 0
    count += count_occurrences(root.left, element)
    count += count_occurrences(root.right, element)
    return count
    
   5) def print_leaf_nodes(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        print(node.value)
    print_leaf_nodes(node.left)
    print_leaf_nodes(node.right)
    
  6)  def count_left_children(node):
    count = 0
    if node.left:
        count += 1
        count += count_left_children(node.left)
        count += count_left_children(node.left.right)
    return count

