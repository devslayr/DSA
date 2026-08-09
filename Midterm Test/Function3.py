# complexity = O(n^2)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def visit(node):
    print(node.value)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        visit(node)
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        visit(node)

def pre_order_traversal(node):
    if node:
        visit(node)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def breadth_first_traversal(root):
    if not root:
        return 
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        visit(current_node)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

# def count_leaf_nodes(root):
#     if not root:
#         return 0
    
#     queue = [root]
#     count = 0
#     while queue:
#         current_node = queue.pop(0)
#         if current_node.left:
#             queue.append(current_node.left)
#         if current_node.right:
#             queue.append(current_node.right)

#         if not current_node.left and not current_node.right:
#             count += 1
#     return count

# complexity = O(n)

def count_leaf_nodes(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.right.left = TreeNode("E")
root.right.right = TreeNode("F")

#       "A"
#       / \
#     "B" "C"
#     /   / \
#   "D" "E" "F"

# breadth_first_traversal(root)
print(count_leaf_nodes(root))