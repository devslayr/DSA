"""----- Function 1 -----"""
# complexity = O(n)
def longest_rising_sublist(readings):
    if not readings:
        return 0
    count = 1
    max_len = 1
    for i in range(len(readings) - 1):
        if readings[i] < readings[i + 1]:
            count += 1
            if count > max_len:
                max_len = count
        else:
            count = 1
    return max_len

"""----- Function 2 -----"""
# complexity = O(n^2)
def process_text_editor(actions):
    output = ""
    for action in actions:
        if action[0] == "type":
            output += action[1]
        if action[0] == "undo":
            output = output[: len(output) - 1]
    return output

"""----- Function 3 -----"""
# complexity = O(n)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_single_child_nodes(root):
    total = 0
    if root is None:
        return
    if not root.left and not root.right:
        return total
    if root.left and not root.right:
        total += root.value
        total += sum_single_child_nodes(root.left)
    elif not root.left and root.right:
        total += root.value
        total += sum_single_child_nodes(root.right)
    elif root.left and root.right:
        total += sum_single_child_nodes(root.left)
        total += sum_single_child_nodes(root.right)
    return total


"""---- Client Code ----"""
if __name__ == '__main__':
    """--- Function 1 ---"""
    numbers = [3, 4, 6, 2, 5, 7, 8, 1]   # Expected output: 4
    # numbers = [5, 5, 5]   # Expected output: 1
    print("Function 1's output:")
    print(longest_rising_sublist(numbers))


    """--- Function 2 ---"""
    actions = [
        ("type", "A"),
        ("type", "B"),
        ("undo",),
        ("type", "C")
    ]   # Expected output: AC

    # actions = [
    #     ("type", "A"),
    #     ("type", "B"),
    #     ("type", "C"),
    #     ("undo",),
    #     ("undo",),
    #     ("type", "D")
    # ]   # Expected output: AD
    print("Function 2's output:")
    print(process_text_editor(actions))


    """--- Function 3 ---"""
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.left.left = TreeNode(6)
    root.right = TreeNode(10)
    root.right.right = TreeNode(14)   # Expected output: 13

    # root = TreeNode(3)
    # root.left = TreeNode(1)
    # root.right = TreeNode(4)   # Expected output: 0

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(9)   # Expected output: 3

    # root = TreeNode(5)
    # root.left = TreeNode(2)
    # root.left.right = TreeNode(4)   # Expected output: 7

    print("Function 3's output:")
    print(sum_single_child_nodes(root))