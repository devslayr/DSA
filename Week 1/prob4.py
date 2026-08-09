# matrix = [
#     [1, 2, 3, 4, 5],
#     [8, 6, 9, 1, 3],
#     [8, 3, 1, 4, 3],
#     [4, 8, 2, 9, 6]
# ]

# # for row in matrix:
# #     for value in row:
# #         print(value, end=" ")
 
# # print(matrix[1][2])
# # print(matrix[2][3])

# top = int(input())
# left = int(input())
# bottom = int(input())
# right = int((input()))

# sum = 0

# for i in range(top, bottom + 1):
#     for j in range (left, right + 1):
#         sum += matrix[i][j]

# print(sum)

"""==================================="""
# Approach 2: precompute the prefix sum of the matrix to make the range sum query faster
# Define: prefix_sum2D[i][j] = sum of all elements in the rectangle defined by (0, 0) and (i, j)
# then, range_sum_query(top, left, bottom, right) = prefix_sum2D[bottom][right] - prefix_sum2D[top-1][right] - prefix_sum2D[bottom][left-1] + prefix_sum2D[top-1][left-1]

matrix = [
  [1, 2, 3, 4, 5],
  [8, 6, 9, 1, 3],
  [8, 3, 1, 4, 3],
  [4, 8, 2, 9, 6]
]

def compute_prefix_sum2D(matrix, queries):
    rows = len(matrix)
    cols = len(matrix[0])
    prefix_sum2D = [[0] * cols for _ in range(rows)]

    prefix_sum2D[0][0] = matrix[0][0]   # top left corner

    for col in range(1, cols):   # first row
        prefix_sum2D[0][col] = prefix_sum2D[0][col - 1] + matrix[0][col]
    
    for row in range(1, rows):   # first column
        prefix_sum2D[row][0] = prefix_sum2D[row - 1][0] + matrix[row][0]

    for row in range(1, rows):
        for col in range(1, cols):
            prefix_sum2D[row][col] = matrix[row][col] + prefix_sum2D[row - 1][col] + prefix_sum2D[row][col - 1] - prefix_sum2D[row - 1][col - 1]

    # print(prefix_sum2D)
    result = []

    for top, left, bottom, right in queries:
        total_sum = prefix_sum2D[bottom][right]
        if top > 0:
            total_sum -= prefix_sum2D[top - 1][right]
        if left > 0:
            total_sum -= prefix_sum2D[bottom][left - 1]
        if top > 0 and left > 0:
            total_sum += prefix_sum2D[top - 1][left - 1]
        result.append(total_sum)
    
    return result

if __name__ == "__main__":
    print(compute_prefix_sum2D(matrix, [(1, 2, 2, 3), (1, 2, 3, 4)]))  # Output: [15, 38]
