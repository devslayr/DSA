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


"""---- Client Code ----"""
if __name__ == '__main__':
    """--- Function 1 ---"""
    # numbers = [3, 4, 6, 2, 5, 7, 8, 1]   # Expected output: 4
    # numbers = [5, 5, 5]   # Expected output: 1
    # print(longest_rising_sublist(numbers))

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
    print(process_text_editor(actions))