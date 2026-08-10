""" ---Function1--- """
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

if __name__ == '__main__':
    """ ---Function1--- """
    # numbers = [3, 4, 6, 2, 5, 7, 8, 1]
    numbers = [5, 5, 5]
    print(longest_rising_sublist(numbers))