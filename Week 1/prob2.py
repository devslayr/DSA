# n = int(input())

# A = []

# for i in range(n):
#     A.append(int(input()))

# for i in range(0, n + 1):
#     if i not in A:
#         print(i)


# n = int(input())
# A = []
# expected_sum = 0
# actual_sum = 0

# for i in range(n):
#     A.append(int(input()))

# for number in A:
#     actual_sum += number

# for j in range(0, n + 1):
#     expected_sum += j

# missing_value = expected_sum - actual_sum

# print(f"The expected sum is: {expected_sum}")
# print("The actual sum is: " + str(actual_sum))
# print("The missing value is:", missing_value)


def find_missing_value(A):
    N = len(A)  # N integers
    expected_sum = N * (N + 1) // 2  # Sum of integers from 0 to N
    actual_sum = sum(A)  # Sum of integers in the list (can use a for loop instead of sum function)
    missing_value = expected_sum - actual_sum  # The missing value is the difference
    return missing_value

print(find_missing_value([0, 3, 2, 4, 1]))  # Output: 5
print(find_missing_value([1, 5, 2, 4, 3]))  # Output: 0
print(find_missing_value([4, 0, 1, 5, 2]))  # Output: 3