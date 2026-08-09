A = [5, 8, 6, 7, 7, 9, 3]
N = len(A)
count = 0

for i in range(1, N):
    if A[i] > A[i - 1] and A[i] > A[i + 1]:
        count += 1

print(count)
