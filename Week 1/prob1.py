A = [7, 6, 9, 3, 2, 5]

max = A[0]

for i in range(len(A)):
    if max < A[i]:
        max = A[i]

print(max)


# A = [7, 6, 9, 3, 2, 5]

# second_max = A[0]
# max = A[1]

# for i in range(len(A)):
#     if second_max > max:
#         temp = second_max
#         second_max = max
#         max = temp
#     if second_max < A[i]:
#         if max > A[i]:
#             second_max = A[i]
#         elif max < A[i]:
#             second_max = max
#             max = A[i]

# print(second_max)

